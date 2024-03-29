import json
import datetime


# Currently a dummy report generated using the sample report from
# https://www.jfrog.com/confluence/display/XRAY1X/Xray+REST+API#XrayRESTAPI-GetSecurityReport

report = {
  "recent_vulnerabilities": {
    "2019-08-29": 1
  },
  "recent_components": {},
  "top_vulnerabilities": [
    {
      "summary": "CWE-20 Improper Input Validation",
      "description": "The MultipartStream class in Apache Commons Fileupload before 1.3.2, as used in Apache Tomcat 7.x before 7.0.70, 8.x before 8.0.36, 8.5.x before 8.5.3, and 9.x before 9.0.0.M7 and other products, allows remote attackers to cause a denial of service (CPU consumption) via a long boundary string.",
      "severity": "Critical",
      "properties": {
        "cve": "CVE-2016-3092",
        "cvss_v2": "7.8",
        "description": "The MultipartStream class in Apache Commons Fileupload before 1.3.2, as used in Apache Tomcat 7.x before 7.0.70, 8.x before 8.0.36, 8.5.x before 8.5.3, and 9.x before 9.0.0.M7 and other products, allows remote attackers to cause a denial of service (CPU consumption) via a long boundary string.",
        "publish_date": "2016-07-04T18:59:04.000Z",
        "references": [
          "http://svn.apache.org/viewvc?view=revision&revision=1743480",
          "http://svn.apache.org/viewvc?view=revision&revision=1743722",
        ],
        "summary": "CWE-20 Improper Input Validation"
      },
      "created": "2016-07-04T18:59:04Z",
      "affected_components": [
        {
          "id": "gav://org.apache.tomcat:tomcat-servlet-api:8.0.32"
        },
        {
          "id": "gav://org.apache.tomcat:tomcat-api:8.0.32"
        },
      ],
    },
  ],
  "top_artifacts": [
    {
      "name": "artifactory-pro-war-4.x-20160616.132515-1.war",
      "path": "/org/artifactory2/pro/artifactory-pro-war/4.x-SNAPSHOT/",
      "package_type": "Maven",
      "indexed": "2016-12-07T14:13:14Z",
      "vulnerabilities": [
        {
          "id": "584818fcaee4940008425415",
          "summary": "The authenticated-encryption feature in the symmetric-encryption implementation in the OWASP Enterprise Security API (ESAPI) for Java 2.x before 2.1.0 does not properly resist tampering with serialized ciphertext"
        },
        {
          "id": "5820903652a576000835b360",
          "summary": "CWE-399 Resource Management Errors"
        },
      ],
    },
  ],
  "lastUpdate":  datetime.datetime.today().strftime("%Y-%m-%dT%H:%M:%SZ")
}


with open('../reports/jfrog-xray-report.json', 'w+') as f:
    json.dump(report, f)
