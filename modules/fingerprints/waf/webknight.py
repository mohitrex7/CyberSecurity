

import re

class Webknight():
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'Webknight',item[1],re.I) is not None
            if _:
                return "WebKnight Application Firewall (AQTRONIX)"
                break
