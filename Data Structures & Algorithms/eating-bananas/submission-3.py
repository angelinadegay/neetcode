class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        

        while left < right:
            k = (right + left) // 2
            total = 0

            for p in piles:
                total += math.ceil(p / k)

            if total > h:
                left = k + 1
            else:
                    right = k

        return left
        

        