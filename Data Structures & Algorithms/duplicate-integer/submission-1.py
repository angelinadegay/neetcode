class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_m = {}

        for n in nums:
            if n in hash_m:
                return True
            else:
                hash_m[n] = 1
        return False
                