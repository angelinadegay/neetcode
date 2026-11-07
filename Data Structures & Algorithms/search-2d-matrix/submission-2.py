class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] < target:
                continue
            else:
                if target in row:
                    return True
        return False
        