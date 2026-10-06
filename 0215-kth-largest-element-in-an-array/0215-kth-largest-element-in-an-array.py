import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        self.heap=[]
        self.k=k
        for i in nums:
            heapq.heappush(self.heap,i)
            if len(self.heap)>k:
                heapq.heappop(self.heap)

        return self.heap[0]