from urllib.parse import urlparse
from bs4 import BeautifulSoup
from utilities.page_info import GetPageInfo
from utilities.url_scrapper import FetchUrl


class BeautifulSoupContentScrapper:
    """
    A class for scraping and extracting externally loaded resources from HTML content using BeautifulSoup.

    Attributes:
        __url (str): The default url to be used Across the System
        __default_parser (str): The default parser to be used by BeautifulSoup.

    Methods:
        fetch_index_page(content):
            Fetches and returns a BeautifulSoup instance for the given HTML content.

        scrape_index_page(url):
            Scrapes the index page from the given URL and extracts externally loaded resources.
    """

    def __init__(self, url=None):
        """
        Initialize the BeautifulSoupContentScrapper instance.
        """
        if url:
            self.__url = url
        else:
            self.__url = "https://www.cfcunderwriting.com"
        self.__default_parser = "html.parser"

    def get_url(self):
        return self.__url

    def get_parser(self):
        return self.__default_parser

    def fetch_index_page(self, content):
        """
        Fetches and returns a BeautifulSoup instance for the given HTML content.

        Args:
            content (str): The HTML content of a webpage.

        Returns:
            BeautifulSoup: A BeautifulSoup instance representing the parsed HTML content.
        """

        # Create a BeautifulSoup instance using the provided HTML content and default parser
        soup_instance = BeautifulSoup(content, self.get_parser())
        return soup_instance

    def scrape_index_page(self):
        """
        Scrapes the index page from the given URL and extracts externally loaded resources.

        Args:

        Returns:
            dict: List of externally loaded resources.
        """

        # Get the url from which the content is to be fetched
        url = self.get_url()

        # Get the content of the webpage using the GetPageInfo class
        get_page = GetPageInfo(url)
        content = get_page.get_content()

        # Fetch the index page by creating a BeautifulSoup instance
        soup = self.fetch_index_page(content)

        # Extract the base URL from the provided URL
        base_url = urlparse(url).scheme + '://' + urlparse(url).netloc

        # Fetch external resources and urls
        bs_scrapper = FetchUrl()

        # external_resources_tags = bs_scrapper.scrape_using_tags(soup, base_url)

        external_resources_re = bs_scrapper.scrape_using_regex(content)
        return external_resources_re

