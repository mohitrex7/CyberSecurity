
import re

class Anquanboa:
	@staticmethod
	def run(headers):
		_ = False
		for item in headers.items():
			_  = re.search(r'X-Powered-By-Anquanbao',item[0],re.I) is not None
			if _:
				return "Anquanbao Firewall"
				break
