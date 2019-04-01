import requests
from requests import Request


def auth_header_value(username, password):
    return "{}_{}".format(username, password)


class MyAuth(requests.auth.AuthBase):
    # http://docs.python-requests.org/en/master/user/authentication/#new-forms-of-authentication
    # http://docs.python-requests.org/en/master/_modules/requests/auth/
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __call__(self, r):
        # Implement my authentication
        r.headers["Authorization"] = auth_header_value(self.username, self.password)
        return r


def test_requests_mock():
    user = "u1"
    password = "p1"
    auth = MyAuth(user, password)
    url = "https://url.com/"
    # http://docs.python-requests.org/en/master/user/advanced/
    prepared_request = Request("GET", url)
    prepared_request_with_auth = auth.__call__(prepared_request)
    assert prepared_request_with_auth.headers["Authorization"] == "{}_{}".format(
        user, password
    )
