import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os
base_dir = "img"
base_url = "https://apod.nasa.gov/apod/archivepix.html"
page = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(page, 'lxml')
#print(soup)
tags = soup.findAll("a")
for tag in tags:
	href = urljoin(base_url,tag["href"])
	print("Need to download... " + href)
	content = urllib.request.urlopen(href)
	for img in BeautifulSoup(content, 'lxml').findAll("img"):
		img_href = urljoin(href, img["src"])
		print("downloading... ", img_href)
		img_name = img_href.split("/")[-1]
		try:
			urllib.request.urlretrieve(img_href, os.path.join(base_dir,img_name))
			break
		except:
			print("Exception in " + img_name)
			pass
		
	

