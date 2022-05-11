from lib.logic.get_candlestick import GetCandlestick


class TestGetCandlestick():

    def setup(self):
        self.APIModel = GetCandlestick()

    def teardown_function(self):
        self.APIModel.release_api()

    def test_get_candlestick_in_valid_timeframe(self):
        """
        use for testing all valid timeframe
        """

        ## Given
        available_parameter = ("1m", "5m", "15m", "30m", "1h", "4h", "6h", "12h", "1D", "7D", "14D", "1M")

        ## When

        ## Then
        for timeframe in available_parameter:
            self.APIModel.modify_timeframe(timeframe)
            self.APIModel.compose_full_url()
            response = self.APIModel.request.send_request()
            self.APIModel.release_api()
            assert response.status_code == 200
            assert self.APIModel.check_response_code_is_valid_or_not(response.json()) is True

    def test_get_candlestick_in_invalid_timeframe(self):
        """
        use for testing invalid timeframe
        """

        ## Given

        ## When
        self.APIModel.modify_timeframe("3m")
        self.APIModel.compose_full_url()
        response = self.APIModel.request.send_request()

        ## Then
        assert response.status_code == 200
        assert self.APIModel.check_response_code_is_valid_or_not(response.json()) is False
        assert self.APIModel.check_response_message_is_valid_or_not(response.json()) is False
            