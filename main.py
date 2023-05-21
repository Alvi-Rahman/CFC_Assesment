from utilities.beautiful_soup_scrapper import BeautifulSoupContentScrapper
from utilities.page_info import GetPageInfo
from utilities.url_scrapper import FetchUrl
import csv


class WebScrapper:
    def __init__(self):
        pass

    def scrape(self):

        get_page = GetPageInfo()
        content = get_page.get_content()

        bs_scrapper = BeautifulSoupContentScrapper()
        soup = bs_scrapper.fetch(content)

        url_scrapper = FetchUrl()
        url_list = url_scrapper.fetch_url_list(content.decode("utf-8"))


if __name__ == "__main__":
    scraper_instance = WebScrapper()
    scraper_instance.scrape()

