

import re

class Incapsula():
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _  = re.search(r'incap_ses|visid_incap|Incapsula',item[1],re.I) is not None
            if _:
                return "Incapsula Web Application Firewall (Incapsula/Imperva)"
                break
