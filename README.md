# glowing-broccoli
A python script to download mangas automatically using beautifulsoap and urllib2.
1. Mangas to be downloaded can be added or modified in manga_info.json.
2. Whenever the script runs, it downloads all the new chapters released for the mangas in the list. Modify the value of 'chapter' next to the manga name in the manga_info.json file to the last chapter read so only the chapters released henceforth are downloaded. To download the whole series, change that value to 1.
3. Keeps track of the last chapter downloaded for all the mangas in manga_info.json.
4. Stores the downloaded files in /home/<YOUR_USERNAME>/manga/<MANGA_NAME>/<CHAPTER_NAME>

Only runs on linux.

Prerequisites: python 2.7+ and beautifulsoap library for python.
Run the following command in the terminal to download beautifulsoap library:
apt-get install python-bs4
