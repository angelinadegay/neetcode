class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting = {}
        for n in nums:
            counting[n] = counting.get(n, 0) + 1
        
        sorted_descending = dict(sorted(counting.items(), key=lambda item: item[1], reverse=True))
        updated = list(sorted_descending.keys())

        return updated[:k]