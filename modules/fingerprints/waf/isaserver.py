

import re

class Isaserver:
    @staticmethod
    def run(content):
        _  = False
        _  = re.search(r'The server denied the specified Uniform Resource Locator (URL). Contact the server administrator.',content,re.I) is not None
        _ |= re.search(r'The ISA Server denied the specified Uniform Resource Locator (URL)',content,re.I) is not None
        if _:
        	return "ISA Server (Microsoft)"
