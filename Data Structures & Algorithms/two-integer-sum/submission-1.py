class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashi = {}

        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in hashi:
                return [hashi[diff], i]
            
            hashi[num] = i
            