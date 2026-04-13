class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        total = 0
        L =0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(length, R-L+1)
                total -= nums[L]
                L+=1
        return length if length < float("inf") else 0