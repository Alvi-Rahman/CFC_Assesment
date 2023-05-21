"""
Privacy Policy Word Count Controller

This module contains the PrivacyPolicyWordCountController class that handles the scraping and word count functionality
for the Privacy Policy page.

Classes:
- PrivacyPolicyWordCountController

"""

from controllers.base import BaseController


class PrivacyPolicyWordCountController(BaseController):
    """
    PrivacyPolicyWordCountController is responsible for scraping the index webpage, extracting externally loaded
    resources, and performing a word count on the visible text of the Privacy Policy page.

    Attributes:
        file_name (str): The name of the output file for external resources.

    Methods:
        __init__(file_name=None):
            Initializes the PrivacyPolicyWordCountController instance.
        __scrape_resources():
            Scrapes the index webpage and extracts externally loaded resources.
        __write_resources():
            Writes the external resources to a JSON file.
        main():
            Main entry point of the controller.

    """

    def __init__(self, file_name=None):
        """
        Initialize the PrivacyPolicyWordCountController instance.

        Args:
            file_name (str): The name of the output file for external resources. If not provided, "external_resources.json"
                             will be used as the default file name.

        """
        if not file_name:
            file_name = "external_resources.json"
        super(PrivacyPolicyWordCountController, self).__init__(file_name)

    def __scrape_resources(self):
        """
        Scrape the index webpage and extract externally loaded resources.

        Returns:
            dict: Dictionary of externally loaded resources categorized by resource type.

        """
        external_resources = self.base_scrapper.scrape_index_page()
        return external_resources

    def __write_resources(self):
        """
        Write the externally loaded resources to a JSON file.

        Returns:
            str: A message indicating the success of writing the resources to the file.

        """
        external_resources = self.__scrape_resources()
        self.file_writer_obj.write_to_json_file(
            external_resources,
            self.file_name
        )
        return f"External resources were written to {self.file_name}"

    def main(self):
        """
        Main entry point of the PrivacyPolicyWordCountController.

        Returns:
            str: A message indicating the success of writing the external resources to the file.

        """
        return self.__write_resources()
