class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for n in nums:
            freq[n] =  freq.get(n,0) + 1
        # for [i,v] in freq.items():
        #     if v >= k:
        #         res.append(i)

        # bucket sort
        buckets = [[] for _ in range(len(nums)+1)]
        for num, count in freq.items():
            buckets[count].append(num)

        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res


        return res
        