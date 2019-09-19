import datetime
import sys

# Currently a dummy report generated using the sample report from
# https://www.jfrog.com/confluence/display/XRAY1X/Xray+REST+API#XrayRESTAPI-GetSecurityReport
# This report indicates the depedency passes the scan
report = {
  "recent_vulnerabilities": {},
  "recent_components": {},
  "top_vulnerabilities": [],
  "top_artifacts": [],
  "lastUpdate":  datetime.datetime.today().strftime("%Y-%m-%dT%H:%M:%SZ")
}

if 'recent_vulnerabilities' in report and \
    len(report['recent_vulnerabilities']) > 0:
  sys.exit(1)

sys.exit(0)
