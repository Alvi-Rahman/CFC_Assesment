from bs4 import BeautifulSoup


class BeautifulSoupContentScrapper:
    def __init__(self):
        self.default_lib = "html5lib"

    @staticmethod
    def fetch(content):
        soup_instance = BeautifulSoup(content, 'html5lib')
        return soup_instance
