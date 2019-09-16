import json
import sys


if __name__ == "__main__":
  with open("../reports/jfrog-xray-report.json", "r") as f:
    report = json.load(f)

  if "recent_vulnerabilities" in report and \
      len(report["recent_vulnerabilities"]) > 0:
    sys.exit(1)

  sys.exit(0)
