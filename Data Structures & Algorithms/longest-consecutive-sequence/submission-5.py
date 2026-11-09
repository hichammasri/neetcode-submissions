class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_s = set(nums)
        starts_of_seq = []
        longest = 0
        for num in nums_s: 
            if (num-1) not in nums_s:
                length = 1
                i = num
                while i+1 in nums_s:
                    length+=1
                    i+=1
                longest = max(longest, length)
        return longest

        
        