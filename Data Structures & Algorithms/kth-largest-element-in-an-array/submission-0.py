import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        idx = 0
        max_ele = 0
        heapq.heapify(arr)

        for n in nums:
            heapq.heappush(arr, -n)
        
        while idx < k:
            max_ele = -heapq.heappop(arr)
            idx +=1
        
        return max_ele
