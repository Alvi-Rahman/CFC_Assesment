import re


class FetchUrl:
    """
    A class for fetching URLs from content based on a specified pattern.

    Attributes:
        __url_pattern (str): The regular expression pattern to match URLs.

    Methods:
        get_url_pattern():
            Returns the URL pattern used for matching.

        fetch_url_list(content):
            Fetches and returns a list of URLs from the provided content.

        get_unique_url_list(url_list):
            Returns a list of unique URLs from the given URL list.
    """

    def __init__(self, pattern=None):
        """
        Initialize the FetchUrl instance.

        Args:
            pattern (str, optional): The regular expression pattern to match URLs.
                                    If not provided, a default pattern is used.
        """
        if pattern:
            self.__url_pattern = pattern
        else:
            self.__url_pattern = r"\b(https?:\/\/(?!.*(?:cfc\.com|cfcunderwriting\.com))[^\s/$.?#]*[^\s\"'><]*)\b"

    def get_url_pattern(self):
        """
        Returns the URL pattern used for matching.

        Returns:
            str: The URL pattern.
        """
        return self.__url_pattern

    def fetch_url_list(self, content):
        """
        Fetches and returns a list of URLs from the provided content.

        Args:
            content (str): The content from which to fetch URLs.

        Returns:
            list: List of URLs.
        """

        # Find all URLs matching the URL pattern in the content
        url_list = re.findall(self.get_url_pattern(), content)
        return self.get_unique_url_list(url_list)

    @staticmethod
    def get_unique_url_list(url_list):
        """
        Returns a list of unique URLs from the given URL list.

        Args:
            url_list (list): The list of URLs.

        Returns:
            list: List of unique URLs.
        """

        # Remove duplicates and return the unique URLs
        return list(set(url_list))
