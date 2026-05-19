class Solution:
    def simulation(self):
        print(self.max_num)
        x = -heapq.heappop(self.max_num)
        y = -heapq.heappop(self.max_num)
       
        if y < x:
            y = x - y
            heapq.heappush(self.max_num, -y)
            print(x,y)
        


    def lastStoneWeight(self, stones: List[int]) -> int:
        self.max_num = [-n for n in stones]
       
        heapq.heapify(self.max_num)
        while len(self.max_num)>1:
            self.simulation()
        print(self.max_num)
        return -self.max_num[0] if len(self.max_num) > 0 else 0