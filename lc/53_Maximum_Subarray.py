from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        first_pos = -1
        for i, n in enumerate(nums):
            if n > 0:
                first_pos = i
                break
        if first_pos == -1:
            return max(nums)
        nums = nums[first_pos:]
        count = len(nums)
        if count == 1:
            return nums[0]

        nl = [0]
        flag = True
        for i, n in enumerate(nums):
            if flag and n > 0:
                nl[-1] += n
                continue
            if n == 0:
                continue
            if not flag and n < 0:
                nl[-1] += n
                continue
            if flag and n < 0:
                nl.append(n)
                flag = False
                continue
            if not flag and n > 0:
                nl.append(n)
                flag = True
                continue


        res = 0
        last_res = 0
        for i, n in enumerate(nl):
            if n > 0:
                res += n
                continue
            if res + n <= 0:
                last_res = res
                res = 0
                continue
            if res + n > 0:
                res += n
                continue
        import ipdb; ipdb.set_trace()
        return max(res, last_res)



    def maxSubArrayOld(self, nums: List[int]) -> int:
        print(nums)
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], (nums[i - 1]+ nums[i]))
        print(nums)
        return max(nums)


if __name__ == "__main__":
    s = Solution()
    # data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # data = [-2, 1, -3, 4, -1, 2, 1, 55, 4]
    data = [-1, -2]
    data = [1, -1, 1]
    r = s.maxSubArrayOld(data)
    print(r)
