class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checking = {}
        for i in range(len (nums)):
            if nums[i] in checking:
                j = checking[nums[i]]
                return [j, i]

            diff = target - nums[i]
            checking[diff] = i
