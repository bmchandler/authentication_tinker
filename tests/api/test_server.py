import pytest
from api import server

USER_ID = 123

def test_get_user_by_id():
    expected = f"User ID: {USER_ID}"
    actual = server.get_user_by_id(USER_ID)
    assert actual == expected