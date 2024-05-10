class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = n + nums[l] + nums[r]
                if three_sum < 0: l += 1
                elif three_sum > 0: r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
        return res
