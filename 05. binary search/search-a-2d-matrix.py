from typing import List

"""
Time Complexity: O(log(n))
Space Complexity: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        start, end = 0, row*col-1
        while start <= end:
            mid = (start+end) // 2
            if matrix[mid//col][mid % col] > target:
                end = mid-1
            elif matrix[mid//col][mid % col] < target:
                start = mid+1
            else:
                return True
        return False
