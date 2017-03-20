import configparser
import pytest
import requests

@pytest.fixture
def conf():
    config = configparser.ConfigParser()
    config.read('manifest.ini')
    return config


def test_heartbeat_fields(env, conf):
    response = requests.get(conf.get(env, 'we_server_url') + '/__heartbeat__')
    data = response.json()
    fields = {'storage', 'portier', 'cache', 'attachments', 'permission', 'oauth'}

    for field in data:
        assert field in fields

def test_version(env, conf):
    response = requests.get(conf.get(env, 'we_server_url') + '/__version__')
    data = response.json()
    fields = {'build', 'commit', 'name', 'source', 'version'}

    for field in data:
        assert field in fields


