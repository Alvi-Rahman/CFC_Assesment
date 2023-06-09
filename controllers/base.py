"""
Base Controller

This module contains the BaseController class that serves as the base controller for other controllers.

Classes:
- BaseController

"""

from utilities.beautiful_soup_scrapper import BeautifulSoupContentScrapper
from utilities.writer import FileWriter


class BaseController:
    """
    BaseController serves as the base controller for other controllers. It provides common functionalities such as
    file writing and content scraping.

    Attributes:
        file_writer_obj (FileWriter): An instance of the FileWriter class for writing files.
        file_name (str): The name of the output file.
        base_scrapper (BeautifulSoupContentScrapper): An instance of the BeautifulSoupContentScrapper class for
                                                     scraping HTML content.
        log_file (str): The name of the error log file.

    Methods:
        __init__(file_name=None):
            Initializes an instance of the BaseController.

    """

    def __init__(self, file_name=None):
        """
        Initializes an instance of the BaseController.

        Args:
            file_name (str, optional): The name of the output file. If not provided, the file_name will be None.

        """
        self.file_writer_obj = FileWriter()
        self.file_name = file_name
        self.base_scrapper = BeautifulSoupContentScrapper()
        self.log_file = "error.log"
