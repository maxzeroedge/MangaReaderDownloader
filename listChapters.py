import requests
from bs4 import BeautifulSoup as bs
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

class ListChapters:
	def __init__(self, url):
		self.siteHtml = requests.get(url).text
		self.siteSoup = bs(self.siteHtml, "html.parser")
	
	def get_chapters(self, url_prefix="https://www.mangareader.net"):
		chapter_list = self.siteSoup.find('div', id="chapterlist")
		chapter_list = chapter_list.find('table', id="listing").find_all("tr")
		self.chapters = []
		for chapter in chapter_list:
			chapter_a = chapter.find("a")
			if(chapter_a != None):
				self.chapters.append({
					"url": url_prefix + chapter_a.attrs["href"],
					"name": chapter_a.text
				})
		return self.chapters



if __name__ == "__main__":
	list_chapters = ListChapters("https://www.mangareader.net/log-horizon")
	list_chapters.get_chapters()
	print(list_chapters.chapters)
