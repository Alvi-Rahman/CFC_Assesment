import pytest
from bs4 import BeautifulSoup
from utilities.url_scrapper import FetchUrl


class TestFetchUrl:
    @pytest.fixture
    def fetch_url(self):
        """
        Fixture for creating an instance of FetchUrl for testing.
        """
        return FetchUrl()

    def test_get_url_pattern(self, fetch_url):
        """
        Test case for the get_url_pattern method of FetchUrl.

        Tests the behavior of returning the URL pattern used for matching.

        Args:
            fetch_url (FetchUrl): Instance of FetchUrl.
        """
        url_pattern = fetch_url.get_url_pattern()

        assert isinstance(url_pattern, str)
        assert len(url_pattern) > 0

    def test_fetch_url_list(self, fetch_url):
        """
        Test case for the fetch_url_list method of FetchUrl.

        Tests the behavior of fetching and returning a list of URLs from the provided content.

        Args:
            fetch_url (FetchUrl): Instance of FetchUrl.
        """
        content = """
        <html>
            <head>
                <title>CFC UnderWriting</title>
            </head>
            <body>
                <a href="https://cfc.com">Link 1</a>
                <a href="https://1234.com/page">Link 2</a>
                <a href="https://test.com/page">Link 3</a>
            </body>
        </html>
        """

        flag, url_list = fetch_url.fetch_url_list(content)

        assert flag is True
        assert isinstance(url_list, list)
        assert len(url_list) == 2
        assert "https://1234.com/page" in url_list
        assert "https://test.com/page" in url_list

    def test_get_unique_url_list(self, fetch_url):
        """
        Test case for the get_unique_url_list method of FetchUrl.

        Tests the behavior of returning a list of unique URLs from the given URL list.

        Args:
            fetch_url (FetchUrl): Instance of FetchUrl.
        """
        url_list = [
            "https://cfc.com",
            "https://cfc.com/page",
            "https://cfc.com",
            "https://cfc.com/page",
        ]

        unique_url_list = fetch_url.get_unique_url_list(url_list)

        assert isinstance(unique_url_list, list)
        assert len(unique_url_list) == 2
        assert "https://cfc.com" in unique_url_list
        assert "https://cfc.com/page" in unique_url_list

    def test_scrape_using_regex(self, fetch_url):
        """
        Test case for the scrape_using_regex method of FetchUrl.

        Tests the behavior of extracting external resources from the provided content using regular expressions.

        Args:
            fetch_url (FetchUrl): Instance of FetchUrl.
        """
        content = """
        <html>
            <head>
                <link rel="stylesheet" href="https://cfc.com/styles.css">
                <link rel="stylesheet" href="https://1234.com/styles.css">
            </head>
            <body>
                <img src="https://cfc.com/image.jpg" alt="Image">
                <img src="https://test.com/image.jpg" alt="Image">
                <script src="https://cfc.com/script.js"></script>
                <script src="https://test.com/script.js"></script>
            </body>
        </html>
        """

        flag, external_resources = fetch_url.scrape_using_regex(content)

        assert flag is True
        assert isinstance(external_resources, dict)
        assert len(external_resources["images"]) == 1
        assert external_resources["images"][0] == "https://test.com/image.jpg"
        assert len(external_resources["scripts"]) == 1
        assert external_resources["scripts"][0] == "https://test.com/script.js"
        assert len(external_resources["stylesheets"]) == 1
        assert external_resources["stylesheets"][0] == "https://1234.com/styles.css"
        assert len(external_resources["links"]) == 0

    def test_find_privacy_policy_url(self, fetch_url):
        """
        Test case for the find_privacy_policy_url method of FetchUrl.

        Tests the behavior of finding the URL of the Privacy Policy page on the given webpage.

        Args:
            fetch_url (FetchUrl): Instance of FetchUrl.
        """
        content = """
        <html>
            <head>
                <title>CFC UnderWriting</title>
            </head>
            <body>
                <a href="/en-gb/support/privacy-policy/">Privacy Policy</a>
                <a href="/en-gb/support/terms">Terms of Service</a>
            </body>
        </html>
        """

        soup = BeautifulSoup(content, "html.parser")
        url = "https://cfc.com"

        flag, privacy_policy_url = fetch_url.find_privacy_policy_url(soup, url)

        assert flag is True
        print("--privacy_policy_url--" + privacy_policy_url)
        assert privacy_policy_url == "https://cfc.com/en-gb/support/privacy-policy/"
