

from utils import output
from request import request
from request import urlcheck

class Bfile:
	def __init__(self,agent,proxy,redirect,timeout,url,cookie):
		self.url = url
		self.cookie = cookie
		self.output = output.Output()
		self.ucheck = urlcheck.UrlCheck()
		self.request = request.Request(
			agent = agent,
			proxy = proxy,
			redirect = redirect,
			timeout = timeout
			)
	
	def run(self):
		info = {
		'name'        : 'Bfile',
		'fullname'    : 'Backup Files',
		'author'      : 'Momo Outaadi (M4ll0k)',
		'description' : 'Find Backup Files'
		}
		self.output.test('Checking common backup files..')
		db = open('data/bfile.txt','rb')
		dbfiles = [x.split('\n') for x in db]
		db1 = open('data/cfile.txt','rb')
		dbfiles1 = [x.split('\n') for x in db1]
		try:
			for b in dbfiles:
				for d in dbfiles1:
					bdir = b[0].replace('[name]',d[0])
					url = self.ucheck.path(self.url,bdir)
					resp = self.request.send(
						url = url,
						method = "GET",
						payload = None,
						headers = None,
						cookies = self.cookie
						)
					if resp.status_code == 200:
						if resp.url == url.replace(' ','%20'):
							self.output.plus('Found file "%s" Backup at %s'%(d[0],resp.url))
		except Exception,e:
			print e
