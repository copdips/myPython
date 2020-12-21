import datetime
import subprocess
import sys
from operator import attrgetter
from pathlib import Path
from typing import Any, List, Optional, Tuple

# import re
# from itertools import combinations
# from typing import List
#
# import pytest
#

class Solution:
    def checkValidString(self, s: str) -> bool:
        balances = {0}
        for c in s:
            print("c:", c, "in balances:", balances)
            tmp = set(balances) if c == '*' else set()
            if c == '*' or c == '(':
                tmp.update({y+1 for y in balances})
            if c == '*' or c == ')':
                tmp.update({y-1 for y in balances if y > 0})
            balances = tmp
            print("out balances:", balances)
        print("==============final balances:", balances)
        return 0 in balances


@pytest.mark.parametrize(
    "s,expected",
    [
        ("(*))", True),
        ("()*", True),
        ("())()*", False),
        ("(*)()*", True),
        ("(())((())()()(*)(*()(())())())()()((()())((()))(*", False),
    ],
)
def test_sol(s, expected):
    # Solution().productExceptSelf(s)
    assert Solution().checkValidString(s) == expected


if __name__ == "__main__":
    test_sol([0, 0], [0, 0])
