#! /usr/bin/python
import urllib2
import urllib
import requests
from bs4 import BeautifulSoup
manga='one-piece'
chapter =871
page=1
while page in range(1,20):
	pageDirectory=manga+'/'+str(chapter)+'/'+str(page)
	link='http://www.mangapanda.com/'+pageDirectory
	pageLink=urllib2.urlopen(link)
	soup = BeautifulSoup(pageLink, "lxml")
	imageLink=soup.find('img', id='img').get("src")
	#urllib.urlretrieve(imageLink, "image.jpg")
	with open(str(page)+'.jpg', 'wb') as handle:
        	response = requests.get(imageLink, stream=True)

        	if not response.ok:
        	    print response

        	for block in response.iter_content(1024):
        	    if not block:
        	        break

        	    handle.write(block)
	page = page+1;
	print imageLink

