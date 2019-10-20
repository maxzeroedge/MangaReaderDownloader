import requests
from os import path, makedirs

class DownloadImage:
	def download_image(self, url):
		url_split = url.split("/")[::-1]
		file_name = url_split[0]
		# print(url_split)
		folder_name = url_split[2]
		folder_name = path.join("__dl", folder_name)
		makedirs(folder_name, exist_ok=True)
		f = open( path.join(folder_name, file_name) ,'wb')
		f.write( requests.get(url).content )
		f.close()