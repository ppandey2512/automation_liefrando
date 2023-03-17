import http
import pytest
from api_wrapper.wrapper import CoopsApi



class TestAuthFail:
    def test_invalid_token(self, config):
        """
        No authorization token: 401
        """
        user = CoopsApi(config['home_url'], config['user_info']['id'])
        user._token = 'Bearer USERTOKEN'
        result = user.get_user()
        assert result.status_code == http.HTTPStatus.UNAUTHORIZED
       
    def test_no_token(self, config):
        """
        No authorization token: 401
        """
        user = CoopsApi(config['home_url'], config['user_info']['id'])
        result = user.unlock_barn()
        try:
            if result.status_code == http.HTTPStatus.UNAUTHORIZED:
                assert True
        except AssertionError:
            assert False
        assert  False

    def test_valid_token_invalid_user_id(self, config):
        """
        No authorization token: 401
        """
        user = CoopsApi(config['home_url'], config['user_info']['id'])
        user.authenticate(config['auth_url'], config['client_id'], config['client_secret'])
        user._user_id = 'pppppppp'
        result = user.unlock_barn()
        assert result.status_code == http.HTTPStatus.UNAUTHORIZED