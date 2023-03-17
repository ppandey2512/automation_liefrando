import http
import pytest
from json_checker import Or
from api.wrapper import CoopsApi
from utils.timer import repeat_until
from api.config import config


@pytest.fixture(scope='session')
def user(config):
    api = CoopsApi(config['home_url'], config['user_info']['id'])
    api.authenticate(config['auth_url'], config['client_id'], config['client_secret'])
    return api


class TestBarn:

    def test_unlock_barn(self, user, config):
        resp = user.unlock_barn()
        assert resp.status_code == http.HTTPStatus.OK

    def test_toilet_seat_down(self, user, config):
        resp = user.put_down_toilet_seat()
        assert resp.status_code == http.HTTPStatus.OK

    def test_feed_chickens(self, user, config):
        resp = user.feed_chickens()
        assert resp.status_code == http.HTTPStatus.OK


    def test_count_eggs(self, user, config):
        resp = user.count_eggs()
        assert resp.status_code == http.HTTPStatus.OK
        

    def test_collect_eggs(self, user, config):
        resp = user.collect_eggs()
        assert resp.status_code == http.HTTPStatus.OK


    def test_count_after_collect(self, user, config):
        intial_count = user.count_eggs()
        eggs_before_collection = intial_count.json()['data'] or 0
        timeout = 30
        eggs_collected = repeat_until(
            lambda: user.collect_eggs().json()['data'] or 0,
            lambda res: res > 0,
            timeout=timeout,
            poll_frequency=1,
        )

        if eggs_collected == 0:
            pytest.skip("No eggs collected within {timeout} seconds.")

        final_count = user.count_eggs()
        eggs_after_collect = final_count.json()['data'] or 0
        assert eggs_after_collect == eggs_before_collection + eggs_collected,  "Wrong count of egss"
          




    
