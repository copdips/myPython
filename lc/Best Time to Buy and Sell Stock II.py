from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        final = 0
        prev = prices[0]
        for n in prices:
            if n == prev:
                continue
            if n > prev:
                final = final + n - prev
            prev = n
        return final


if __name__ == "__main__":
    data = [7, 1, 5, 3, 6, 4]
    print(data)
    print(Solution().maxProfit(data))
