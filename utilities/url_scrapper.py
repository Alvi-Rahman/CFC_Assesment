import re


class FetchUrl:
    def __init__(self, pattern=None):
        if pattern:
            self.__url_pattern = pattern
        else:
            self.__url_pattern = r"\b(https?:\/\/(?!.*(?:cfc\.com|cfcunderwriting\.com))[^\s/$.?#]*[^\s\"'><]*)\b"

    def get_url_pattern(self):
        return self.__url_pattern

    def fetch_url_list(self, content):
        url_list = re.findall(self.get_url_pattern(), content)
        return self.get_unique_url_list(url_list)

    @staticmethod
    def get_unique_url_list(url_list):
        return list(set(url_list))
