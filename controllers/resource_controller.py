"""
ResourceScrapeController

A controller class for scraping external resources from a webpage and writing the results to a JSON file.

Attributes:
    file_name (str): The name of the output JSON file.

Methods:
    __scrape_resources():
        Scrapes external resources from a webpage.
    __write_resources():
        Writes the scraped external resources to a JSON file.
    main():
        Entry point of the controller.

Inherits:
    BaseController
"""

from controllers.base import BaseController


class ResourceScrapeController(BaseController):
    def __init__(self, file_name=None):
        """
        Initialize the ResourceScrapeController instance.

        Args:
            file_name (str, optional): The name of the output JSON file.
                                       If not provided, a default name is used.
        """
        if not file_name:
            file_name = "privacy_policy_word_count.json"
        super(ResourceScrapeController, self).__init__(file_name)

    def __scrape_resources(self):
        """
        Scrapes external resources from a webpage.

        Returns:
            dict: Dictionary containing the scraped external resources.
        """
        external_resources = self.base_scrapper.scrape_index_page()
        return external_resources

    def __write_resources(self):
        """
        Writes the scraped external resources to a JSON file.

        Returns:
            str: Message indicating the success of the write operation.
        """
        external_resources = self.__scrape_resources()
        self.file_writer_obj.write_to_json_file(
            external_resources,
            self.file_name
        )
        return f"External resources were written to {self.file_name}"

    def main(self):
        """
        Entry point of the controller.

        Returns:
            str: Message indicating the success of the operation.
        """
        return self.__write_resources()
