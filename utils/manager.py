from crawler import crawler
from modules.fingerprints import checkall
from modules.discovery.brute import brute
from modules.discovery.other import other
from modules.discovery.vulns import vulns
from modules.discovery.attack import attack
from modules.discovery.disclosure import disclosure

def fingerprints(agent,proxy,redirect,timeout,url,cookie):
	checkall.Checkall(
		agent = agent,
		proxy = proxy,
		redirect = redirect,
		timeout = timeout,
		url = url,
		cookie = cookie
		).run()

def crawling(agent,proxy,redirect,timeout,url,cookie):
	return crawler.Crawler(
		agent = agent,
		proxy = proxy,
		redirect = redirect,
		timeout = timeout,
		url = url,
		cookie = cookie
		).process()

def bruteforce(agent,proxy,redirect,timeout,url,cookie):
	brute.Brute(
		agent = agent,
		proxy = proxy,
		redirect = redirect,
		timeout = timeout,
		url = url,
		cookie = cookie
		).run()

def others(agent,proxy,redirect,timeout,url,cookie):
	other.Other(
		agent = agent,
		proxy = proxy,
		redirect = redirect,
		timeout = timeout,
		url = url,
		cookie = cookie
		).run()

def vuln(agent,proxy,redirect,timeout,url,cookie):
	vulns.Vulns(
		agent = agent,
		proxy = proxy,
		redirect = redirect,
		timeout = timeout,
		url = url,
		cookie = cookie
		).run()

def attacks(agent,proxy,redirect,timeout,url,cookie):
	attack.Attack(
		agent = agent,
		proxy = proxy,
		redirect = redirect,
		timeout = timeout,
		url = url,
		cookie = cookie
		).run()

def disc(agent,proxy,redirect,timeout,url,cookie):
	disclosure.Disclosure(
		agent = agent,
		proxy = proxy,
		redirect = redirect,
		timeout = timeout,
		url = url,
		cookie = cookie
		).run()
