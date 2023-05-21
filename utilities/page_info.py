import requests


class GetPageInfo:

    def __init__(self, url):
        self.__page_url = url

    def get_url(self):
        return self.__page_url

    def send_get_request(self):
        response = requests.get(self.get_url())
        return response

    def get_content(self):
        response = self.send_get_request()
        return response.text
