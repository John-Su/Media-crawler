import torlock

s = torlock.webSite('https://163.com')
s.crawl(s.url)
s.save_tor()
s.save_source()
s.save_outSide()
n = 0
for url in s.outside_list:
	site = torlock.webSite(url)
	try:
		site.crawl(site.url)
	except Exception:
		continue
	site.save_tor()
	site.save_source()
	site.save_outSide()
	n = n + 1 
	if (n > 10):
		break
