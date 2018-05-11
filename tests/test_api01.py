import pytest
from conftest import scenario1, scenario2

class TestLogin(object):
    scenarios = [scenario1, scenario2]

    def test_login_01(self, URL):
        assert "www" in URL

    def test_login_02(self, URL):
        assert "ok" == "ok"

    def test_login_03(self, URL):
        assert "sohu" in URL
