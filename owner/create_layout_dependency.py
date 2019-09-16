# Inspired by / Copied from:
# https://github.com/in-toto/demo/blob/master/owner_alice/create_layout.py


from in_toto.util import import_rsa_key_from_file
from in_toto.models.layout import Layout
from in_toto.models.metadata import Metablock


def main():
  key_owner = import_rsa_key_from_file("dependency_owner")
  key_developer = import_rsa_key_from_file("../developer/developer.pub")
  key_reviewer = import_rsa_key_from_file("../reviewer/reviewer.pub")

  layout = Layout.read({
      "_type": "layout",
      "keys": {
          key_developer["keyid"]: key_developer,
          key_reviewer["keyid"]: key_reviewer,
      },
      "steps": [{
          "name": "dependency-develop",
          "expected_materials": [],
          "expected_products": [
            ["CREATE", "../dependency/demo.py"],
            ["DISALLOW", "*"]
          ],
          "pubkeys": [key_developer["keyid"]],
          "expected_command": [],
          "threshold": 1,
        },{
          "name": "dependency-code-review",
          "expected_materials": [
            ["MATCH", "../dependency/demo.py", "WITH", "PRODUCTS", "FROM",
              "dependency-develop"],
            ["DISALLOW", "*"]
          ],
          "expected_products": [
            ["ALLOW", "../dependency/demo.py"],
            ["DISALLOW", "*"]
          ],
          "pubkeys": [key_reviewer["keyid"]],
          "expected_command": [],
          "threshold": 1,
        },
      ],
      "inspect": [],
  })

  metadata = Metablock(signed=layout)

  # Sign and dump layout to "root.layout"
  metadata.sign(key_owner)
  metadata.dump("../metadata_dependency/root.layout")

if __name__ == '__main__':
  main()
