#! /usr/bin/python
import urllib2
import urllib
import json
import requests
from bs4 import BeautifulSoup
INFO_FILE='manga_info.json'
#manga='one-piece'
#chapter =871
#page=18
with open(INFO_FILE, 'r') as f:
	pyDict=json.load(f)
noOfMangas= len(pyDict)
for i in range(0,noOfMangas,1):
	manga=pyDict[i]['manga']
	chapter=pyDict[i]['chapter']
	page =1
	checker=0
	while checker != 1:
		pageDirectory=manga+'/'+str(chapter)+'/'+str(page)
		link='http://www.mangapanda.com/'+pageDirectory
		print link
		try:
			pageLink=urllib2.urlopen(link)
		except urllib2.HTTPError, e:
			print(e.code)
			chapter = chapter + 1;
			pyDict[i]['chapter'] = chapter
			page = 1
			continue
		soup = BeautifulSoup(pageLink, "lxml")
		imageLinkString=soup.find('img', id='img')
		#print imageLinkString
		if str(imageLinkString) != 'None':
			checker = 0;
			imageLink=imageLinkString.get("src")
			#somehow the following line doesn't work
			#urllib.urlretrieve(imageLink, "image.jpg")
			with open(manga+'-'+str(chapter)+'-'+str(page)+'.jpg', 'wb') as handle:
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
			#the manga has not been released yet or has been concluded
			with open(INFO_FILE, 'w') as out:
    				json.dump(pyDict, out)
			checker =1
