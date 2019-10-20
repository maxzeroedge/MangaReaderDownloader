import requests
from bs4 import BeautifulSoup as bs
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

class ListPages:
	def __init__(self, url):
		self.siteHtml = requests.get(url).text
		self.siteSoup = bs(self.siteHtml, "html.parser")
	
	def get_pages(self, url_prefix="https://www.mangareader.net"):
		page_list = self.siteSoup.find('div', id="selectpage")
		page_list = page_list.find('select', id="pageMenu").find_all("option")
		self.pages = []
		self.current_page = 1
		for page_item in page_list:
			self.pages.append({
				"url": url_prefix + page_item.attrs["value"],
				"name": page_item.text
			})
			# print(page_item.attrs)
			if(page_item.attrs.get("selected", False)):
				self.current_page = page_item.text
		return self.pages

	def get_current_page_image(self):
		image_item = self.siteSoup.find("div", id="imgholder")
		image_item = image_item.find("img", id="img")
		return image_item.attrs["src"]


if __name__ == "__main__":
	list_pages = ListPages("https://www.mangareader.net/log-horizon/1/5")
	list_pages.get_pages()
	print(list_pages.pages)
	print(list_pages.current_page)
	print(list_pages.get_current_page_image())
