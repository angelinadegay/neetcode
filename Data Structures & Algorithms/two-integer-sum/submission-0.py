class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSum = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashSum:
                return [hashSum[diff], i]
            hashSum[n] = i
        return
        