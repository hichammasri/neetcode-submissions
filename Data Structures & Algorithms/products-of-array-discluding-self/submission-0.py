class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        cum_prod = [1]+ [p:= p * num for num in nums]

        p = 1
        cum_prod_rev = [1] + [p:= p * num for num in nums[::-1]]

        n = len(nums)

        prod_except_self = [cum_prod[i]*cum_prod_rev[n-1-i] for i in range(n)]

        return prod_except_self

