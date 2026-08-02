class Solution(object):
    def twoSum(self, nums, target):
        notebook = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in notebook:
                return[notebook[needed],i]
            notebook[nums[i]] = i
        