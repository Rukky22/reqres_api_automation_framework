import yaml
import pytest
from core.api_client import APIClient
from core.user_api import USER_API

@pytest.fixture(scope = "session")
def config():
    with open("../config/dev.yaml", "r") as file:
        return yaml.safe_load(file)


@pytest.fixture(scope = "session")
def api_client(config):
    base_url = config['base_url']
    timeout = config['timeout']
    api_key = config["api_key"]
    return APIClient(base_url=base_url, timeout=timeout, api_key=api_key)


@pytest.fixture(scope = "session")
def user_api(api_client):
    return USER_API(api_client)