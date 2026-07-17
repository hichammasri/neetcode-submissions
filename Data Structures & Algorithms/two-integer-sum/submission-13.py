class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        elements_indices = {}

        for i in range(len(nums)):
            num = nums[i]
            elements_indices.setdefault(num, []).append(i)
        for element in elements_indices:
            remaining = target - element
            if (remaining == element):
                if len(elements_indices[remaining]) > 1:
                    return elements_indices[remaining][:2]
                else:
                    continue
            if remaining in elements_indices:
                i1 = elements_indices[element][0]
                i2 = elements_indices[remaining][0]
                return [i1, i2]


