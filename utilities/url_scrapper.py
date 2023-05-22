"""
FetchUrl

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
    scrape_using_tags(soup, base_url):
        Extracts external resources from the BeautifulSoup instance using HTML tags.
    scrape_using_regex(content):
        Extracts external resources from the provided content using regular expressions.
    find_privacy_policy_url(soup, url):
        Finds the URL of the Privacy Policy page on the given webpage.
"""

import re
from urllib.parse import urlparse


class FetchUrl:
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
            tuple: A tuple containing a flag indicating success (bool) and a List of URLs.
        """

        # Find all URLs matching the URL pattern in the content
        try:
            url_list = re.findall(self.get_url_pattern(), content)
            return True, self.get_unique_url_list(url_list)
        except Exception as e:
            return False, e.args[0]

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

    @staticmethod
    def scrape_using_tags(soup, base_url):
        """
        Extracts external resources from the BeautifulSoup instance using HTML tags.

        Args:
            soup (BeautifulSoup): The BeautifulSoup instance representing the parsed HTML content.
            base_url (str): The base URL of the webpage.

        Returns:
            tuple: A tuple containing a flag indicating success (bool) and a dict containing the extracted external resources.
        """
        try:
            external_resources = {
                'img': [],
                'script': [],
                'fonts': [],
                'link': [],
            }
            resource_tags = soup.find_all(['img', 'script', 'link'])

            for tag in resource_tags:
                resource_url = None
                resource_type = tag.name

                if resource_type == 'img':
                    resource_url = tag.get('src')
                elif resource_type == 'script':
                    resource_url = tag.get('src')
                    external_resources.setdefault(resource_type, [])
                elif resource_type == 'link' and tag.get('rel') == ['stylesheet'] or tag.get('rel') == 'stylesheet':
                    resource_url = tag.get('href')
                elif resource_type == 'link' and tag.get('rel') == 'preload' and tag.get('as') == 'font':
                    resource_url = tag.get('href')

                if resource_url and not resource_url.startswith('/') and not resource_url.startswith(base_url) \
                        and not resource_url.startswith('https://cfc.com'):
                    external_resources[resource_type].append(resource_url)

            return True, external_resources
        except Exception as e:
            return False, e.args[0]

    def scrape_using_regex(self, content):
        """
        Extracts external resources from the provided content using regular expressions.

        Args:
            content (str): The content from which to extract external resources.

        Returns:
            tuple: A tuple containing a flag indicating success (bool) and a Dictionary containing the extracted external resources.
        """
        try:
            external_resources = {
                'images': [],
                'scripts': [],
                'stylesheets': [],
                'fonts': [],
                'links': [],
            }

            image_types = ['jpg', 'png', 'svg', 'jpeg']
            script_types = ['js']
            stylesheet_types = ['css']
            fonts = ['https://fonts']

            # Fetch external resources and urls
            flag, url_list = self.fetch_url_list(content)

            if not flag:
                return flag, url_list

            # Loop for Mapping and generating Json File for External Resources
            for url in url_list:
                url_lookup = url.lower().split('.')
                if url_lookup[-1] in image_types:
                    external_resources['images'].append(url)
                elif url_lookup[-1] in script_types:
                    external_resources['scripts'].append(url)
                elif url_lookup[-1] in stylesheet_types:
                    external_resources['stylesheets'].append(url)
                elif url_lookup[0] in fonts:
                    external_resources['fonts'].append(url)
                else:
                    external_resources['links'].append(url)

            return True, external_resources
        except Exception as e:
            return False, e.args[0]

    @staticmethod
    def find_privacy_policy_url(soup, url):
        """
        Finds the URL of the Privacy Policy page on the given webpage.

        Args:
            soup (BeautifulSoup): The BeautifulSoup instance representing the parsed HTML content.
            url (str): The URL of the webpage.

        Returns:
            str: The URL of the Privacy Policy page.
        """
        try:
            # Find all <a> tags and search for the Privacy Policy link
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if 'privacy' in href.lower() and 'policy' in href.lower():
                    privacy_policy_url = urlparse(url)._replace(path=href).geturl()
                    return True, privacy_policy_url

            return False, None
        except Exception as e:
            return False, e.args[0]
