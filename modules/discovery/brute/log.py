

import re

from utils import output
from request import request
from request import urlcheck

class Log:
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
		'name'        : 'Log',
		'fullname'    : 'Logs File',
		'author'      : 'Momo Outaadi (M4ll0k)',
		'description' : 'Find Logs file'
		}
		self.output.test('Checking common log files..')
		db = open('data/log.txt','rb')
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
						self.output.plus('Found log file at %s'%(resp.url))
		except Exception,e:
			print e
