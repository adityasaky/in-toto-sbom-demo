# Inspired by / Copied from:
# https://github.com/in-toto/demo/blob/master/owner_alice/create_layout.py


from in_toto.util import import_rsa_key_from_file
from in_toto.models.layout import Layout
from in_toto.models.metadata import Metablock


def main():
  key_owner = import_rsa_key_from_file("owner")
  key_developer = import_rsa_key_from_file("../developer/developer.pub")
  key_reviewer = import_rsa_key_from_file("../reviewer/reviewer.pub")
  key_xray = import_rsa_key_from_file("../xray/xray.pub")

  layout = Layout.read({
      "_type": "layout",
      "keys": {
          key_developer["keyid"]: key_developer,
          key_reviewer["keyid"]: key_reviewer,
          key_xray["keyid"]: key_xray,
      },
      "steps": [{
          "name": "develop",
          "expected_materials": [],
          "expected_products": [
            ["CREATE", "../target/demo.py"],
            ["DISALLOW", "*"]
          ],
          "pubkeys": [key_developer["keyid"]],
          "expected_command": [],
          "threshold": 1,
        },{
          "name": "code-review",
          "expected_materials": [
            ["MATCH", "../target/demo.py", "WITH", "PRODUCTS", "FROM",
              "develop"],
            ["DISALLOW", "*"]
          ],
          "expected_products": [
            ["ALLOW", "../target/demo.py"],
            ["DISALLOW", "*"]
          ],
          "pubkeys": [key_reviewer["keyid"]],
          "expected_command": [],
          "threshold": 1,
        },{
          "name": "jfrog-xray",
          "expected_materials": [
            ["MATCH", "../target/demo.py", "WITH", "PRODUCTS", "FROM",
              "develop"],
            ["DISALLOW", "*"],
          ],
          "expected_products": [
              ["CREATE", "../reports/jfrog-xray-report.json"],
              ["DISALLOW", "*"],
          ],
          "pubkeys": [key_xray["keyid"]],
          "expected_command": ["python", "generate_report.py"],
          "threshold": 1,
        },
      ],
      "inspect": [{
        "name": "check-vulnerability-report",
        "expected_materials": [
          ["MATCH", "../reports/jfrog-xray-report.json", "WITH", "PRODUCTS",
            "FROM", "jfrog-xray"]
        ],
        "expected_products": [],
        "run": ["python", "scripts/validate_jfrog_xray_report.py"]
      }],
  })

  metadata = Metablock(signed=layout)

  # Sign and dump layout to "root.layout"
  metadata.sign(key_owner)
  metadata.dump("../metadata/root.layout")

if __name__ == '__main__':
  main()
