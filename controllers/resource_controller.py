"""
Resource Scrape Controller

This module contains the ResourceScrapeController class that handles scraping and counting words in the privacy policy.

Classes:
- ResourceScrapeController

"""

from controllers.base import BaseController


class ResourceScrapeController(BaseController):
    """
    ResourceScrapeController handles the scraping of resources and counting words in the privacy policy.

    Attributes:
        file_name (str): The name of the output file.

    Methods:
        __init__(file_name=None):
            Initializes the ResourceScrapeController instance.
        __get_privacy_policy_word_count():
            Retrieves the word count of the privacy policy from the base scrapper.
        __write_privacy_policy_word_count():
            Writes the privacy policy word count to a JSON file.
        main():
            Main entry point of the ResourceScrapeController class.

    """

    def __init__(self, file_name=None):
        """
        Initialize the ResourceScrapeController instance.

        Args:
            file_name (str): The name of the output file. If not provided, the file_name will be None.

        """
        if not file_name:
            file_name = "external_resources.json"
        super(ResourceScrapeController, self).__init__(file_name)

    def __get_privacy_policy_word_count(self):
        """
        Retrieve the word count of the privacy policy from the base scrapper.

        Returns:
            dict: A dictionary containing the word count of the privacy policy.

        """
        privacy_policy_word_count = self.base_scrapper.privacy_policy_word_frequency_counter()
        return privacy_policy_word_count

    def __write_privacy_policy_word_count(self):
        """
        Write the privacy policy word count to a JSON file.

        Returns:
            str: A message indicating the success of writing the privacy policy word count.

        """
        privacy_policy_word_count = self.__get_privacy_policy_word_count()
        self.file_writer_obj.write_to_json_file(
            privacy_policy_word_count, self.file_name)
        return f"Privacy Policy Count was written to {self.file_name}"

    def main(self):
        """
        Main entry point of the ResourceScrapeController class.

        Returns:
            str: A message indicating the success of writing the privacy policy word count.

        """
        return self.__write_privacy_policy_word_count()
