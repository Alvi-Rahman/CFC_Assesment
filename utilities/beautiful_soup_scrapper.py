"""
BeautifulSoupContentScrapper

A class for scraping and extracting externally loaded resources from HTML content using BeautifulSoup.

Attributes:
    __url (str): The default URL to be used across the system.
    __default_parser (str): The default parser to be used by BeautifulSoup.

Methods:
    fetch_bs_page(content):
        Fetches and returns a BeautifulSoup instance for the given HTML content.
    scrape_index_page():
        Scrapes the index page from the given URL and extracts externally loaded resources.
    count_words_frequency(url):
        Scrapes the webpage at the given URL, performs case-insensitive word frequency count on the visible text,
        and returns the frequency count as a dictionary.
    privacy_policy_word_frequency_counter():
        Scrapes the privacy policy page from the given URL, performs case-insensitive word frequency count on the
        visible text, and returns the frequency count as a dictionary.
"""

from bs4 import BeautifulSoup
from utilities.page_info import GetPageInfo
from utilities.url_scrapper import FetchUrl


class BeautifulSoupContentScrapper:
    def __init__(self, url=None):
        """
        Initialize the BeautifulSoupContentScrapper instance.

        Args:
            url (str, optional): The default URL to be used across the system. Defaults to "https://www.cfcunderwriting.com".
        """
        if url:
            self.__url = url
        else:
            self.__url = "https://www.cfcunderwriting.com"
        self.__default_parser = "html.parser"

    def get_url(self):
        """
        Get the default URL.

        Returns:
            str: The default URL.
        """
        return self.__url

    def get_parser(self):
        """
        Get the default parser.

        Returns:
            str: The default parser.
        """
        return self.__default_parser

    def fetch_bs_page(self, content):
        """
        Fetches and returns a BeautifulSoup instance for the given HTML content.

        Args:
            content (str): The HTML content of a webpage.

        Returns:
            BeautifulSoup: A BeautifulSoup instance representing the parsed HTML content.
        """
        soup_instance = BeautifulSoup(content, self.get_parser())
        return soup_instance

    def scrape_index_page(self):
        """
        Scrapes the index page from the given URL and extracts externally loaded resources.

        Returns:
            dict: Dictionary of externally loaded resources.
        """
        url = self.get_url()
        get_page = GetPageInfo(url)
        content = get_page.get_content()
        soup = self.fetch_bs_page(content)

        bs_scrapper = FetchUrl()
        external_resources = bs_scrapper.scrape_using_regex(content)

        return external_resources

    def count_words_frequency(self, url):
        """
        Scrapes the webpage at the given URL, performs case-insensitive word frequency count on the visible text,
        and returns the frequency count as a dictionary.

        Args:
            url (str): The URL of the webpage.

        Returns:
            dict: Dictionary containing word frequency count.
        """
        try:
            get_page = GetPageInfo(url)
            content = get_page.get_content()
            soup = self.fetch_bs_page(content)

            visible_text = soup.get_text()
            visible_text = visible_text.replace('\n', ' ')
            visible_text = visible_text.split()
            visible_text = [text.strip() for text in visible_text]

            word_count = {}
            for text in visible_text:
                words = text.lower().split()
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1

            return word_count
        except Exception as e:
            print(f"Error occurred while counting word frequency: {e}")

    def privacy_policy_word_frequency_counter(self):
        """
        Scrapes the privacy policy page from the given URL, performs case-insensitive word frequency count on the
        visible text, and returns the frequency count as a dictionary.

        Returns:
            dict: Dictionary containing word frequency count of the privacy policy page.
        """
        try:
            url = self.get_url()
            get_page = GetPageInfo(url)
            content = get_page.get_content()
            soup = self.fetch_bs_page(content)

            bs_scrapper = FetchUrl()
            privacy_policy_url = bs_scrapper.find_privacy_policy_url(soup, url)

            word_count = self.count_words_frequency(privacy_policy_url)
            return word_count
        except Exception as e:
            print(f"Error occurred while counting word frequency: {e}")
