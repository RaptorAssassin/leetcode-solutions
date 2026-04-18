import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        result = 0
        for _ in range(k):
            result = heapq.heappop(max_heap) * -1
        return result
