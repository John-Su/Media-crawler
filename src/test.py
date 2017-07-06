import website
import Base

Crawled=set()
site = 'http://bbc.com'
back = 0
def pealthesite(site):
	s = website.webSite(site)
	s.crawl(s.url)
	'''
	if len(s.tor_list) > 1:
		s.save_tor()
	if len(s.source_list) > 1:
		s.save_source()
	if len(s.outside_list) > 1:
		s.save_outSide()
	if len(s.inside_list) > 1:
		s.save_inSide()
	'''
	n = 0
	for url in s.outside_list:
		if Base.existUrl(url,6):
			print ('[info]Back at: ' + url + ' from: ' + site)
			back += 1
			print(back)
			if (back > 10):
				print('ok')
				exit()
		try:
			pealthesite(url)
		except Exception:
			continue
		n = n + 1 
		if (n > 10):
			break

pealthesite(site)
