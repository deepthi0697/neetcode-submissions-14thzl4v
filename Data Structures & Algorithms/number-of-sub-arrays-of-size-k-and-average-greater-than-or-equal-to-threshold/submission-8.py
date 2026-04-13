class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res,sub = [],[]
        i,avg=0,0
        for j in range(len(arr)):
            if j-i+1 > k:
                avg -= sub[0]
                sub = sub[1:]
                i+=1
            avg += arr[j]
            sub.append(arr[j])
            if j-i+1 == k and avg/k >= threshold:
                res.append(sub)
        return len(res)
