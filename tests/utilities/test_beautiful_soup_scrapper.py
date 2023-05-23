import pytest
from bs4 import BeautifulSoup
from utilities.beautiful_soup_scrapper import BeautifulSoupContentScrapper


class TestBeautifulSoupContentScrapper:
    @pytest.fixture
    def beautifulsoup_content_scrapper(self):
        """
        Fixture for creating an instance of BeautifulSoupContentScrapper for testing.
        """
        return BeautifulSoupContentScrapper()

    def test_fetch_bs_page(self, beautifulsoup_content_scrapper):
        """
        Test case for the fetch_bs_page method of BeautifulSoupContentScrapper.

        Tests the behavior of fetching and returning a BeautifulSoup instance for the given HTML content.

        Args:
            beautifulsoup_content_scrapper (BeautifulSoupContentScrapper): Instance of BeautifulSoupContentScrapper.
        """
        content = "<html><body><h1>CFC UnderWriting</h1></body></html>"
        flag, soup_instance = beautifulsoup_content_scrapper.fetch_bs_page(content)
        assert flag is True
        assert isinstance(soup_instance, BeautifulSoup)

    def test_scrape_index_page(self, beautifulsoup_content_scrapper):
        """
        Test case for the scrape_index_page method of BeautifulSoupContentScrapper.

        Tests the behavior of scraping the index page from the default URL and extracting externally loaded resources.

        Args:
            beautifulsoup_content_scrapper (BeautifulSoupContentScrapper): Instance of BeautifulSoupContentScrapper.
        """
        flag, external_resources = beautifulsoup_content_scrapper.scrape_index_page()
        assert flag is True
        assert isinstance(external_resources, dict)

    def test_count_words_frequency(self, beautifulsoup_content_scrapper):
        """
        Test case for the count_words_frequency method of BeautifulSoupContentScrapper.

        Tests the behavior of scraping a webpage at the given URL, performing case-insensitive word frequency count on the visible text,
        and returning the frequency count as a dictionary.

        Args:
            beautifulsoup_content_scrapper (BeautifulSoupContentScrapper): Instance of BeautifulSoupContentScrapper.
        """
        url = "https://cfcunderwriting.com/"
        flag, word_count = beautifulsoup_content_scrapper.count_words_frequency(url)
        assert flag is True
        assert isinstance(word_count, dict)

    def test_privacy_policy_word_frequency_counter(self, beautifulsoup_content_scrapper):
        """
        Test case for the privacy_policy_word_frequency_counter method of BeautifulSoupContentScrapper.

        Tests the behavior of scraping the privacy policy page from the default URL, performing case-insensitive word frequency count on the visible text,
        and returning the frequency count as a dictionary.

        Args:
            beautifulsoup_content_scrapper (BeautifulSoupContentScrapper): Instance of BeautifulSoupContentScrapper.
        """
        flag, word_count = beautifulsoup_content_scrapper.privacy_policy_word_frequency_counter()
        assert flag is True
        assert isinstance(word_count, dict)
