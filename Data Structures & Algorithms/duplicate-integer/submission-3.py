class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for n in nums:
            if n in check:
                return True
            check[n] = 1
        return False
        