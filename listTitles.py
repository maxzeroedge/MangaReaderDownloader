import requests
from bs4 import BeautifulSoup as bs
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

class ListTitles:
	def __init__(self):
		self.siteHtml = requests.get("https://www.mangareader.net/alphabetical").text
		self.siteSoup = bs(self.siteHtml, "html.parser")
	
	def get_names(self, url_prefix="https://www.mangareader.net"):
		series_alpha_ul_list = self.siteSoup.find_all('ul', class_="series_alpha")
		self.manga_titles = []
		for series_alpha_ul in series_alpha_ul_list:
			series_alpha_li_list = series_alpha_ul.find_all('li')
			for series_alpha_li in series_alpha_li_list:
				self.manga_titles.append( {
					'url': url_prefix + series_alpha_li.find('a').attrs['href'],
					'name': series_alpha_li.find('a').text
				} )
		return self.manga_titles


if __name__ == "__main__":
	list_titles = ListTitles()
	list_titles.get_names()
	print(list_titles.manga_titles)
