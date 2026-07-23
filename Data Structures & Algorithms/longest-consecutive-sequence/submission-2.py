class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        available_nums = set(nums)
        start_nums = []
        for num in nums:
            if num - 1 not in available_nums:
                start_nums.append(num)
        global_max = 1
        for num in start_nums:
            i = num
            local_max = 1
            while i + 1 in available_nums:
                local_max += 1
                i += 1
            if local_max > global_max:
                global_max = local_max
        
        return global_max



                
                

            