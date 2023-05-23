import pytest
import requests
from utilities.page_info import GetPageInfo


class TestGetPageInfo:
    @pytest.fixture
    def get_page_info(self):
        """
        Fixture for creating an instance of GetPageInfo for testing.
        """
        url = "https://www.cfcunderwriting.com"
        return GetPageInfo(url)

    def test_send_get_request(self, get_page_info):
        """
        Test case for the send_get_request method of GetPageInfo.

        Tests the behavior of sending a GET request to the webpage URL and returning the response.

        Args:
            get_page_info (GetPageInfo): Instance of GetPageInfo.
        """
        flag, response = get_page_info.send_get_request()
        assert flag is True
        assert isinstance(response, requests.Response)

    def test_get_content(self, get_page_info):
        """
        Test case for the get_content method of GetPageInfo.

        Tests the behavior of getting the content of the webpage as text.

        Args:
            get_page_info (GetPageInfo): Instance of GetPageInfo.
        """
        flag, content = get_page_info.get_content()
        assert flag is True
        assert isinstance(content, str)
