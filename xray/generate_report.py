import json


# currently a blank report pulled from:
# https://www.jfrog.com/confluence/display/XRAY1X/Xray+REST+API#XrayRESTAPI-GetSecurityReport

report = {
  "lastUpdate": "Time",
  "recent_components": [
    0
  ],
  "recent_vulnerabilities": [
    0
  ],
  "top_artifacts": [
    {
      "indexed": "Time",
      "name": "",
      "package_type": "",
      "path": "",
      "vulnerabilities": [
        {
          "id": {},
          "summary": ""
        }
      ]
    }
  ],
  "top_vulnerabilities": [
    {
      "affected_components": [
        {
          "id": "",
          "impacted_paths": [
            ""
          ]
        }
      ],
      "created": "Time",
      "description": "",
      "properties": [
        "interface"
      ],
      "severity": "",
      "summary": ""
    }
  ]
}


with open('../reports/jfrog-xray-report.json', 'w+') as f:
    json.dump(report, f)
