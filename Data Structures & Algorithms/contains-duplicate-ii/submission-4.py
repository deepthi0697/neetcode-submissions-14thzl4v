class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        res = set()

        for j in range(len(nums)):
            if j - i  > k:
                res.remove(nums[i])
                i +=1
            if nums[j] in res:
                return True
            res.add(nums[j])
        return False
            



