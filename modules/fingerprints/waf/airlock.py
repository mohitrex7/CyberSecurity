

import re

class Airlock:
	@staticmethod
	def run(headers):
		_ = False
		for item in headers.items():
			_  = re.search(r'^AL[_-]SESS[_-]S=\S*',item[1],re.I) is not None
			_ |= re.search(r'X-Airlock-Test',item[0],re.I) is not None
			if _:
				return "InfoGuard Airlock (Phion/Ergon)"
				break
