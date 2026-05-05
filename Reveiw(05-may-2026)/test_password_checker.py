import pytest
from password_checker import is_strong_passowrd
@pytest.mark.parametrize("pwd,expected", [
    ("Abc1234@",True),  #true    # min 8 character should be
    ("ABC123@",False), #no lower case
    ("abc123@",False),  #no upper case
    ("Abcdef@",False),  #no digit
    ("Abc12345",False), # no special char
    ("Abc 123@",False), # space not allowed
])

def test_password(pwd,expected):
    assert is_strong_passowrd(pwd) == expected