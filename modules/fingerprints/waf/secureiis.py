
import re

class Secureiis:
    @staticmethod
    def run(content):
        _ = False
        _  = re.search(r'SecureIIS[^<]+Web Server Protection',content,re.I) is not None
        _ |= re.search(r'http://www.eeye.com/SecureIIS/',content,re.I) is not None
        _ |= re.search(r'\?subject=[^>]*SecureIIS Error',content,re.I) is not None
        if _:
            return "SecureIIS Web Server Security (BeyondTrust"
