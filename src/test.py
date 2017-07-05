import website

Crawled=set()
site = 'http://bbc.com'
def pealthesite(site):
	s = website.webSite(site)
	s.crawl(s.url)
	if len(s.tor_list) > 1:
		s.save_tor()
	if len(s.source_list) > 1:
		s.save_source()
	if len(s.outside_list) > 1:
		s.save_outSide()
	if len(s.inside_list) > 1:
		s.save_inSide()
	Crawled.add(s.url)
	if len(Crawled) > 0:
		exit()
	n = 0
	for url in s.outside_list.difference(Crawled):
		print('Crawlling: ' + url)
		try:
			pealthesite(url)
		except Exception:
			continue
		n = n + 1 
		if (n > 10):
			break

pealthesite(site)
