from utilities.beautiful_soup_scrapper import BeautifulSoupContentScrapper
from utilities.page_info import GetPageInfo
import csv


class WebScrapper:
    def __init__(self):
        pass

    def scrape(self):

        get_page = GetPageInfo()
        content = get_page.get_content()

        bs_scrapper = BeautifulSoupContentScrapper()
        soup = bs_scrapper.fetch(content)


if __name__ == "__main__":
    scraper_instance = WebScrapper()
    scraper_instance.scrape()

