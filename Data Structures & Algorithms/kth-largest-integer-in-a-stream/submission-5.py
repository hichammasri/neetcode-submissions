import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        self.top_k = nums

    def add(self, val: int) -> int:

        heapq.heappush(self.top_k, val)
    
        if len(self.top_k)>self.k:
            heapq.heappop(self.top_k)

        return self.top_k[0]
        
