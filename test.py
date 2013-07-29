from bs4 import BeautifulSoup
import urllib2, httplib

httplib.HTTPConnection.debuglevel = 1

request = urllib2.Request('http://lyrics.wikia.com/Special:Random')



opener = urllib2.build_opener()

f = opener.open(request)
print f.url
#for line in f:
#	print line
	
	