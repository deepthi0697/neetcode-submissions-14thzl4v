class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            curr = 0
            prod = 1
            while curr < len(nums) :
                if curr != i:
                    prod *= nums[curr]
                curr +=1
            res.append(prod)
        return res