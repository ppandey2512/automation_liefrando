import logging
import pytest
import yaml

@pytest.fixture(scope='session')
def config():
    with open('api/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    #print(config)
    return config

