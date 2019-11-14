import re

class UrlExtract:
	@staticmethod
	def run(content):
		try:
			urls = re.findall(r'href=[\'"]?([^\'" >]+)|Allow: (\/.*)|Disallow: (\/.*)|<loc>(.+?)</loc>',content)
			return urls
		except Exception,e:
			pass
