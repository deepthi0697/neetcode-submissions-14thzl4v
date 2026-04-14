class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        diff = float('inf')
        for i,n in enumerate(prices):
            l = i
            r = l+1
            while l<r and l <len(prices) and r < len(prices):
                if prices[l] < prices[r]:
                    diff = prices[r] - prices[l]
                    max_diff = max(max_diff, diff)
                    r+=1
                else:
                    l+=1
                    r+=1
        return max_diff


        