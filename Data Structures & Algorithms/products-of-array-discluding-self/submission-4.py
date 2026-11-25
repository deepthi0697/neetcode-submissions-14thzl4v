class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        # res [1,1,2,8] prefix = 48
            
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix 
            suffix *= nums[i] #24
        # res = [48,24,12,8]
            
        return res