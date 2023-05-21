"""
ResourceScrapeController

A controller class for scraping external resources from a webpage and writing the results to a JSON file.

Attributes:
    file_name (str): The name of the output JSON file.

Methods:
    __scrape_resources():
        Scrapes external resources from a webpage and returns a dictionary of the scraped resources.
    __write_resources():
        Writes the scraped external resources to a JSON file and returns a message indicating the success of the write operation.
    main():
        Entry point of the controller that orchestrates the scraping and writing process.

Inherits:
    BaseController
"""

from controllers.base import BaseController


class ResourceScrapeController(BaseController):
    def __init__(self, file_name=None):
        """
        Initialize the ResourceScrapeController instance.

        Args:
            file_name (str, optional): The name of the output JSON file. If not provided, a default name is used.
        """
        if not file_name:
            file_name = "external_resources.json"
        super(ResourceScrapeController, self).__init__(file_name)

    def __scrape_resources(self):
        """
        Scrapes external resources from a webpage and returns a dictionary of the scraped resources.

        Returns:
            dict: Dictionary containing the scraped external resources.
        """
        try:
            flag, external_resources = self.base_scrapper.scrape_index_page()
            return flag, external_resources
        except Exception as e:
            return False, f"Error Writing file to {self.file_name} due to {e.args}"

    def __write_resources(self):
        """
        Writes the scraped external resources to a JSON file and returns a message indicating the success of the write operation.

        Returns:
            str: Message indicating the success of the write operation or an error message if writing fails.
        """
        try:
            flag, external_resources = self.__scrape_resources()
            if not flag:
                return f"Error Writing file to {self.file_name} due to {external_resources}"
            self.file_writer_obj.write_to_json_file(
                external_resources,
                self.file_name
            )
            return f"External resources were written to {self.file_name}"
        except Exception as e:
            return f"Error Writing file to {self.file_name} due to {e.args}"

    def main(self):
        """
        Entry point of the controller that orchestrates the scraping and writing process.

        Returns:
            str: Message indicating the success of the operation or an error message if an exception occurs.
        """
        try:
            return self.__write_resources()
        except Exception as e:
            self.file_writer_obj.write_logs(
                e.args[0],
                self.log_file
            )
            return f"Error Writing {self.file_name} File"
