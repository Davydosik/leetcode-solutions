class Solution(object):
    def removeDuplicates(self, nums):
        L = 0
        
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[L] = nums[i]
                L += 1
        nums[L] = nums[-1]
        
        return L + 1