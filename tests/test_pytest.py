from dataclasses import dataclass
from unittest.mock import Mock

import pytest
import requests


@pytest.mark.allow_hosts(["54.166.163.67"])
def test():
    requests.get("http://54.166.163.67/status/200")
