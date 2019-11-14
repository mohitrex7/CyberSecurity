class UrlCheck:
	def payload(self,url,payload):
		if url.endswith('/')&payload.startswith('/'):
			return url[:-1]+"?"+payload[1:]
		elif not url.endswith('/')&(payload.startswith('/')):
			return url+"?"+payload[1:]
		elif url.endswith('/')and not(payload.startswith('/')):
			return url[:-1]+"?"+payload 
		else:
			return url+"?"+payload

	def path(self,url,path):
		if url.endswith('/')&path.startswith('/'):
			if not path.endswith('/'):
				return str(url[:-1]+path)
			else:
				return str(url+path[:-1])
		elif not url.endswith('/')and not path.startswith('/'):
			if not path.endswith('/'):
				return str(url+"/"+path)
			else:
				return str(url+"/"+path[:-1])
		else:
			if not path.endswith('/'):
				return str(url+path)
			else:
				return str(url+path[:-1])
