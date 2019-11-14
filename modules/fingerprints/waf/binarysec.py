

import re

class Binarysec():
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _  = re.search(r'BinarySec',item[1],re.I) is not None
            _ |= re.search(r'x-binarysec-[via|nocahe]',item[0],re.I) is not None
            if _:
                return "BinarySEC Web Application Firewall (BinarySEC)"
                break
