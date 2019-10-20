import requests
from os import path, mkdir
from bs4 import BeautifulSoup as bs
from downloadImage import DownloadImage

class DownloadChapter:
	def __init__(self):
		self.downloadImage = DownloadImage()
	
	def get_current_page_image(self, siteSoup):
		image_item = siteSoup.find("div", id="imgholder")
		image_item = image_item.find("img", id="img")
		return image_item.attrs["src"]

	def download_chapter(self, chapter_pages):
		for page in chapter_pages:
			page_item = bs(requests.get(page["url"]).text, "html.parser")
			self.downloadImage.download_image(self.get_current_page_image(page_item))
		return "Done"