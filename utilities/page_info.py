"""
GetPageInfo

A class for fetching webpage information using HTTP GET requests.

Attributes:
    __page_url (str): The URL of the webpage.

Methods:
    get_url():
        Get the URL of the webpage.
    send_get_request():
        Send a GET request to the webpage URL and return the response.
    get_content():
        Get the content of the webpage as text.
"""

import requests


class GetPageInfo:
    def __init__(self, url):
        """
        Initialize the GetPageInfo instance.

        Args:
            url (str): The URL of the webpage.
        """
        self.__page_url = url

    def get_url(self):
        """
        Get the URL of the webpage.

        Returns:
            str: The URL of the webpage.
        """
        return self.__page_url

    def send_get_request(self):
        """
        Send a GET request to the webpage URL and return the response.

        Returns:
            tuple: A tuple containing a flag indicating success (bool) and a requests.Response: The response object returned by the GET request.
        """
        try:
            response = requests.get(self.get_url())
            return True, response
        except Exception as e:
            return False, e.args[0]

    def get_content(self):
        """
        Get the content of the webpage as text.

        Returns:
            tuple: A tuple containing a flag indicating success (bool) and a str: The content of the webpage.
        """
        try:
            flag, response = self.send_get_request()
            return True, response.text
        except Exception as e:
            return False, e.args[0]
