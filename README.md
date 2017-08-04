# glowing-broccoli
A python script to download mangas automatically using beautifulsoap and urllib2.
1. Mangas to be downloaded can be added or modified in manga_info.json.
2. Whenever the script runs, it downloads all the chapters released after the chapter that was last downloaded.
3. Keeps track of the last chapter downloaded for all the mangas in manga_info.json.
4. Store the downloaded files in /home/<USERNAME>/manga/<MANGA_NAME>/<CHAPTER_NAME>

Only runs on linux.

Prerequisites: python 2.7+ and beautifulsoap library for python.
Run the following command in the terminal to download beautifulsoap library:
apt-get install python-bs4
