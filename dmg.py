#! /usr/bin/python
import urllib2
import urllib
import requests
from bs4 import BeautifulSoup
manga='one-piece'
chapter =871
page=1
checker =0
while checker != 2:
	pageDirectory=manga+'/'+str(chapter)+'/'+str(page)
	link='http://www.mangapanda.com/'+pageDirectory
	print link
	pageLink=urllib2.urlopen(link)
	soup = BeautifulSoup(pageLink, "lxml")
	imageLinkString=soup.find('img', id='img')
	#print imageLinkString
	if str(imageLinkString) != 'None':
		checker = 0;
		imageLink=imageLinkString.get("src")
		#somehow the following line doesn't work
		#urllib.urlretrieve(imageLink, "image.jpg")
		with open(str(chapter)+'-'+str(page)+'.jpg', 'wb') as handle:
			response = requests.get(imageLink, stream=True)

			if not response.ok:
			    print response

			for block in response.iter_content(1024):
			    if not block:
			        break

			    handle.write(block)
		page = page+1;
		print imageLink
	else :
		checker=checker+1
		if checker!=2:
			chapter = chapter + 1
			page =1

