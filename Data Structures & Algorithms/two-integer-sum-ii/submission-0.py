class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashSum = {}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in hashSum:
                return [hashSum[diff],i + 1]
            hashSum[n] = i + 1
        return []


        