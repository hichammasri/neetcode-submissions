class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Naive Solution (A)
        frequency = {}
        # O(n)
        for num in nums: 
            frequency[num] = frequency.get(num, 0) + 1

        nums_per_frequency = defaultdict(list)
        # O(n)
        for num in frequency: 
            freq = frequency[num]
            nums_per_frequency[freq].append(num)

        i = len(nums)
        top = []
        while i > 0 and len(top)<k:
            if i in nums_per_frequency: 
                top+=nums_per_frequency[i]
            i-=1
        return top[:k]
        

        # # O(nlogn)
        # sorted_by_freq = dict(sorted(frequency.items(), key= lambda item:item[1], reverse = True))
        # return list(sorted_by_freq.keys())[:k]
    

    


        