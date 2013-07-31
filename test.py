#from bs4 import BeautifulSoup
import urllib2, httplib
import re
httplib.HTTPConnection.debuglevel = 1

request = urllib2.Request('http://lyrics.wikia.com/Special:Random')

i=0
while i<10:

	opener = urllib2.build_opener()

	f = opener.open(request)
	match = re.search(r'LyricFind:(\w+):(\w+)',f.url)

	artist=match.group(1)
	song = match.group(2)
	print f.url
	print artist, song
	i=i+1

