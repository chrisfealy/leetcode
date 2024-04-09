class Solution(object):
    def twoSum(self, nums, target):
        prev_nums = {} # num: index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in prev_nums:
                return [prev_nums[num], i]

            prev_nums[num] = i
