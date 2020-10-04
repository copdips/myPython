from os.path import abspath
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            print("less than 2 stones:", stones)
            return stones
        stones.sort()
        print("stones:", stones)
        last = stones.pop()
        before_last = stones.pop()
        delta = last - before_last
        print("last:", last, "before_last:", before_last, "delta:", delta)
        if delta != 0:
            stones.append(delta)
        return self.lastStoneWeight(stones)


if __name__ == "__main__":
    s = Solution()
    data = [2,7,4,1,8,1]
    r = s.lastStoneWeight(data)
    print(r)
