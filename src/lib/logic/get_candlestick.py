from lib.common.logging import get_logger
from lib.core.rest import RequestManager


class GetCandlestick(object):

    logger = get_logger("GetCandlestick")

    def __init__(self):
        self.parameter = {
            "instrument_name": "",
            "timeframe": ""
        }
        self.request = RequestManager("GET", "get-candlestick", self.parameter)
        self.initial_request()
        self.url = self.request.url

    def initial_request(self):
        self.modify_timeframe()
        self.modify_instrument()

    def release_api(self):
        self.parameter = {
            "instrument_name": "",
            "timeframe": ""
        }
        self.request.url = self.url
        self.initial_request()

    def compose_full_url(self):
        self.request.url = self.request.url + "".join(["{0}={1}&".format(k, v) for k,v in self.parameter.items()])
        self.logger.info("Full URL : {}".format(self.request.url))

    def modify_timeframe(self, timeframe="1m"):
        self.parameter["timeframe"] = timeframe

    def modify_instrument(self, instrument="BTC_USDT"):
        self.parameter["instrument_name"] = instrument

    def check_response_message_is_valid_or_not(self, data):
        if "message" not in data:
            self.logger.info("Message not found, Response: {}".format(data))
            return False
        elif data["message"].find("is not supported") != -1:
            self.logger.info("Can not found message is not supported, Response: {}".format(data["message"]))
            return False
        else:
            return True

    def check_response_code_is_valid_or_not(self, data):
        if "code" not in data:
            self.logger.info("Response: {}".format(data))
            return False
        elif data["code"] != 0:
            self.logger.info("Response: {}".format(data["code"]))
            return False
        else:
            return True
