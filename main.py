from listTitles import ListTitles
from listChapters import ListChapters
from listPages import ListPages
from downloadImage import DownloadImage
from downloadChapter import DownloadChapter
from concurrent.futures.thread import ThreadPoolExecutor

# SAO is 4363
if __name__ == "__main__":
	list_titles = ListTitles()
	title_list = list_titles.get_names()
	for indx, list_title in enumerate(title_list):
		print(indx, list_title["name"])
	selection = input("Select one of the available mangas:")
	selection = int(selection)
	manga_name = title_list[selection]["name"] 
	selection = title_list[selection]["url"]
	list_chapters = ListChapters(selection)
	chapter_list = list_chapters.get_chapters()
	downloadImage = DownloadImage()
	downloadChapter = DownloadChapter()
	with ThreadPoolExecutor(max_workers=4) as executor:
		for chapter in chapter_list:
			list_pages = ListPages(chapter["url"])
			page_list = list_pages.get_pages()
			future = executor.submit(downloadChapter.download_chapter, page_list)
			print(future.result())
			# for page in page_list:
			# 	page_item = ListPages(page["url"])
			# 	downloadImage.download_image(page_item.get_current_page_image())