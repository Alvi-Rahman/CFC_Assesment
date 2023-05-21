"""
PrivacyPolicyWordCountController

A controller class for counting the word frequency in a privacy policy and writing the count to a JSON file.

Attributes:
    file_name (str): The name of the output JSON file.

Methods:
    __get_privacy_policy_word_count():
        Retrieves the word frequency count of the privacy policy and returns a dictionary of the count.
    __write_privacy_policy_word_count():
        Writes the privacy policy word frequency count to a JSON file.
    main():
        Entry point of the controller that orchestrates the word counting and writing process.

Inherits:
    BaseController
"""

from controllers.base import BaseController


class PrivacyPolicyWordCountController(BaseController):
    def __init__(self, file_name=None):
        """
        Initialize the PrivacyPolicyWordCountController instance.

        Args:
            file_name (str, optional): The name of the output JSON file. If not provided, a default name is used.
        """
        if not file_name:
            file_name = "privacy_policy_word_count.json"
        super(PrivacyPolicyWordCountController, self).__init__(file_name)

    def __get_privacy_policy_word_count(self):
        """
        Retrieves the word frequency count of the privacy policy and returns a dictionary of the count.

        Returns:
            dict: Dictionary containing the word frequency count of the privacy policy.
        """
        privacy_policy_word_count = self.base_scrapper.privacy_policy_word_frequency_counter()
        return privacy_policy_word_count

    def __write_privacy_policy_word_count(self):
        """
        Writes the privacy policy word frequency count to a JSON file.

        Returns:
            str: Message indicating the success of the write operation.
        """
        privacy_policy_word_count = self.__get_privacy_policy_word_count()
        self.file_writer_obj.write_to_json_file(
            privacy_policy_word_count, self.file_name)
        return f"Privacy Policy Count was written to {self.file_name}"

    def main(self):
        """
        Entry point of the controller that orchestrates the word counting and writing process.

        Returns:
            str: Message indicating the success of the operation or an error message if an exception occurs.
        """
        try:
            return self.__write_privacy_policy_word_count()
        except Exception as e:
            self.file_writer_obj.write_logs(
                e.args[0],
                self.log_file
            )
            return f"Error Writing {self.file_name} File"
