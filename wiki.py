import urllib2
from bs4 import BeautifulSoup

stdurl = "https://en.wikipedia.org/wiki/"

query = raw_input("Enter what you want to know about: ").split()
furl = stdurl
for i in range(0,len(query)):
	if(i==len(query)-1):
		furl = furl + str(query[i])
	else:
		furl = furl + str(query[i]) + "_"
print furl

try:
	
	res = urllib2.urlopen(furl)
	page = res.read()

	try:
		splitted_page = page.split("<div id=\"mw-content-text\" lang=\"en\" dir=\"ltr\" class=\"mw-content-ltr\">", 1)
		splitted_page = splitted_page[1].split("</table>", 1)
		splitted_page = splitted_page[1].split("</p>", 1)
		soup = BeautifulSoup(splitted_page[0], "html5lib")

		print(soup.get_text())

	except (urllib2.HTTPError): 
		print "404"
except (urllib2.HTTPError):
	stdurl = "https://en.wikipedia.org/wiki/Special:Search?search="
	furl=stdurl
	for i in range(0,len(query)):
		if(i==len(query)-1):
			furl = furl + str(query[i])
		else:
			furl = furl + str(query[i]) + "+"
	print furl
	res = urllib2.urlopen(furl)
	page = res.read()
	
	try:
		splitted_page = page.split("<div class=\"mw-search-result-heading\">", 1)
		splitted_page_new = splitted_page[1].split("</a>", 1)
		soup = BeautifulSoup(splitted_page_new[0], "html5lib")

		print(soup.get_text())
	except:
		print "I've lost control over this"