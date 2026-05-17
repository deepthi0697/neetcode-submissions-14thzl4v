class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < len(nums):
            if nums[l] > nums[r]:
                l += 1
            else:
                return nums[l]
            

        return 0
            