#! /usr/bin/python
import urllib2
import os
import errno
import json
import requests
from bs4 import BeautifulSoup

INFO_FILE = os.path.dirname(os.path.abspath(__file__))+'/manga_info.json'
DEFAULT_LINUX_PATH = '/home/'+os.getlogin()
# DEFAULT_WINDOWS_PATH='C:\\Manga\\'

with open(INFO_FILE, 'r') as f:
	pyDict = json.load(f)
noOfMangas = len(pyDict)
for i in range(0, noOfMangas, 1):
	manga = pyDict[i]['manga']
	chapter = pyDict[i]['chapter']
	page = 1
	checker = 0
	# try creating a directory for the manga if it doesn't exist
	mangaDirectory = DEFAULT_LINUX_PATH+'/manga/'+manga
	try:
		os.makedirs(mangaDirectory)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
	chapterDirectory = 'null'
	while checker != 1:
		pageDirectory = manga+'/'+str(chapter)+'/'+str(page)
		link = 'http://www.mangapanda.com/'+pageDirectory
		try:
			pageLink = urllib2.urlopen(link)
			#print link
			# the following will run on reaching the end of the chapter
		except urllib2.HTTPError, e:
			#print(e.code)
			chapter = chapter + 1
			pyDict[i]['chapter'] = chapter
			page = 1
			continue
		soup = BeautifulSoup(pageLink, "lxml")
		imageLinkString = soup.find('img', id='img')
		# if imageLinkString is not None then it contains an image which will be downloaded
		if str(imageLinkString) != 'None':
	# try creating a directory for the current chapter in the manga if it doesn't exist
			if page == 1:
				try:
					print 'Yay!'
					chapterDirectory = mangaDirectory+'/'+str(chapter)
					os.makedirs(chapterDirectory)
					print "Downloading chapter "+str(chapter)+" of "+manga+"."
				except OSError as e:
					if e.errno != errno.EEXIST:
						raise
			checker = 0
			imageLink = imageLinkString.get("src")
			# somehow the following line doesn't work
			#urllib.urlretrieve(imageLink, "image.jpg")
			with open(chapterDirectory+'/'+str(page)+'.jpg', 'wb') as handle:
				response = requests.get(imageLink, stream=True)

				if not response.ok:
					print response

				for block in response.iter_content(1024):
					if not block:
						break
					handle.write(block)

			page = page + 1
			print imageLink
		else:
			# imageLinkString prints "None" if trying to access a n+1th chapter of manga with n chapters
			print "Chapter "+str(chapter) + " of " + manga + " has not yet been released or the series has been concluded."
			with open(INFO_FILE, 'w') as out:
					json.dump(pyDict, out)
			checker = 1
