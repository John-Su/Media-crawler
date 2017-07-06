#! env: python3
import urllib.request as request
import suSparse

def existUrl(url,n):
	indexofurl = parseurl(url,n)
	dems = []
	for i in range(0,n):
		dems.append(128)
	sp = suSparse.suSparse(dem = dems)
	flag = True
	for i in indexofurl:
		if not sp.getitem(i) == 1:
			flag = False  #not exist
			sp.setitem(i)
		else:
			pass
	return flag

def parseurl(url,n):
	url = request.quote(url)
	indexofurl = []
	for i in range(0, len(url) - n + 1):
		segment = []
		for j in range(0,n):
			segment.append(ord(url[i+j]))
		indexofurl.append(segment)
	return indexofurl 



