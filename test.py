import torlock

s = torlock.torlock()
s.crawl(s.url)
s.save_tor()
s.save_source()
