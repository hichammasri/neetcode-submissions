class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        # O(n)
        for num in nums: 
            frequency[num] = frequency.get(num, 0) + 1
        # O(nlogn)
        sorted_by_freq = dict(sorted(frequency.items(), key= lambda item:item[1], reverse = True))

        return list(sorted_by_freq.keys())[:k]


        