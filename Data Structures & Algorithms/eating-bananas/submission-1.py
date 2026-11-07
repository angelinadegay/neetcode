class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)


        while low < high:
            k = (low + high) // 2
            sum = 0
            for p in piles:
                sum += math.ceil(p/k)
                
            if sum > h:
                low = k + 1
            elif sum <= h:
                high = k
        return low
            
                