import pytest
from conftest import scenario1, scenario2

class TestRegister(object):
    scenarios = [scenario1, scenario2]

    def test_register_01(self, URL):
        assert "com" in URL
    
    def test_register_02(self, URL):
        assert "www" in URL
    
    def test_register_03(self, URL):
        assert "baidu" in URL

    def test_register_04(self, URL):
        assert "good" == "good"