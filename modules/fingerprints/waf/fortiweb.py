

import re

class Fortiweb():
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'FORTIWAFSID=',item[1],re.I) is not None
            if _:
                return "FortiWeb Web Application Firewall (Fortinet)"
                break
