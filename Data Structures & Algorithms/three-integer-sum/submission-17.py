class Solution:

    def twoSums(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        i = 0
        j = len(nums) -1
        doubles = set()
        result = []
        while i < j:
            if nums[i] + nums[j] == target:
                double = (nums[i], nums[j])
                i += 1
                j -= 1
                if double not in doubles:
                    doubles.add(double)
                    result.append(list(double))
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1
        return result


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums_sorted = sorted(nums)
        triplets = set()
        result = []

        for i, num in enumerate(nums_sorted):
            if num > 0 :
                break
            rem = -1*num
            twoSumResult = self.twoSums(nums_sorted[i+1:], rem)
            if twoSumResult:
                for double in twoSumResult:
                    triplet = (num, double[0], double[1],)
                    if triplet not in triplets:
                        triplets.add(triplet)
                        result.append(list(triplet))

        return result


        


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res



        