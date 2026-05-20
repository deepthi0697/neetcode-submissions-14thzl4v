import math
import heapq

class Solution:
    def distance(self,x,y):
        return math.sqrt(x**2 + y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_heap = []
        heapq.heapify(distance_heap)

        for x,y in points:
            distance = self.distance(x,y)
            heapq.heappush(distance_heap,(-distance,[x,y]))
            if len(distance_heap) > k:
                heapq.heappop(distance_heap)

        res = []
        for i in range(len(distance_heap)):
            res.append(heapq.heappop(distance_heap)[1])
        
        return res
        
        