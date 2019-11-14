
import re

from utils import output
from request import request
from request import urlcheck

class File:
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
		'name'        : 'File',
		'fullname'    : 'Common Files',
		'author'      : 'Momo Outaadi (M4ll0k)',
		'description' : 'Find Common Files'
		}
		self.output.test('Checking common files...')
		db = open('data/cfile.txt','rb')
		dbfiles = [x.split('\n') for x in db]
		try:
			for d in dbfiles:
				url = self.ucheck.path(self.url,d[0])
				resp = self.request.send(
					url = url,
					method = "GET",
					payload = None,
					headers = None,
					cookies = self.cookie
					)
				if resp.status_code == 200:
					if resp.url == url.replace(' ','%20'):
						self.output.plus('Found "%s" file at %s'%(d[0],resp.url))
		except Exception,e:
			print e
