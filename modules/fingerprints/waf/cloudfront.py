

import re

class Cloudfront():
    @staticmethod
    def run(headers):
        _ = False
        for item in headers.items():
            _ = re.search(r'(cloudfront)',item[1],re.I) is not None
            _ |= re.search('x-amz-cf-id',item[0],re.I) is not None
            if _: 
                return "CloudFront Web Application Firewall (Amazon)"
                break
