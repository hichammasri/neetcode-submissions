class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        n = len(matrix)
        m = len(matrix[0])
        right = (n * m) - 1

        while left <= right:
            mid = left + (right - left)//2
            i , j = mid//m, mid%m
            if target > matrix[i][j]:
                left = mid + 1
            elif target < matrix[i][j]:
                right = mid - 1
            else:
                return True
        return False

        