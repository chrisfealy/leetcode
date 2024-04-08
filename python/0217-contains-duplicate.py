class Solution(object):
    def containsDuplicate(self, nums):
        dupes = set()
        for num in nums:
            if num in dupes:
                return True
            dupes.add(num)
        return False
