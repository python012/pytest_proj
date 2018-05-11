import pytest


class TestLogin(object):

    @pytest.mark.parametrize("test_input,expected", [
        ("3+5", 8),
        ("2+4", 6)])
    def test_login_01(self, test_input, expected):
        assert eval(test_input) == expected

    def test_login_02(self):
        assert "ok" == "ok"

    def test_login_03(self):
        assert "successful" == "successful"
