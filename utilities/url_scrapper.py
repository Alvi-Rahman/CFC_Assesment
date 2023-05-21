import re
from urllib.parse import urlparse


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

    @staticmethod
    def scrape_using_tags(soup, base_url):
        # List to store the external resources
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

        return external_resources

    def scrape_using_regex(self, content):
        # List to store the external resources
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
        url_list = self.fetch_url_list(content)

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

        return external_resources

    @staticmethod
    def find_privacy_policy_url(soup, url):
        """
        Finds the URL of the Privacy Policy page on the given webpage.

        Args:
            soup (BeautifulSoup): BS4 instance for the webpage to be scraped
            url (str): url from which privacy policy is to be scraped

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
                    return privacy_policy_url

            print("Privacy Policy page not found.")
        # except requests.exceptions.RequestException as e:
        except Exception as e:
            print(f"Error occurred while finding the Privacy Policy URL: {e}")
