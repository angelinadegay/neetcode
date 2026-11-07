class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            sum = 0
            for pile in piles:
                sum += math.ceil(pile / mid)

            if sum > h:
                left = mid + 1
            else:
                right = mid
        return left
        