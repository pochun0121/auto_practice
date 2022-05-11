from lib.common.logging import get_logger
import requests


class RequestManager(object):

    ALLOW_METHODS = ("GET", "POST", "PUT", "DELETE")
    logger = get_logger("RequestManager")

    def __init__(self, method, api_name, param):
        self.host = "https://api.crypto.com/v2/"
        self.method = method
        self.api_name = api_name
        self.param = param
        self.url = self.compose_url()

    def compose_url(self):
        full_url = self.host + "public/" + self.api_name + "?"
        self.logger.info("Full URL : {}".format(full_url))
        return full_url

    def send_request(self):
        print(self.url)
        if self.method == "GET":
            response = requests.get(self.url)
        elif self.method == "POST":
            response = requests.post(self.url)

        if response.status_code == 200:
            return response
        else:
            self.logger.debug("request status code : {}".format(response.status_code))
            return False