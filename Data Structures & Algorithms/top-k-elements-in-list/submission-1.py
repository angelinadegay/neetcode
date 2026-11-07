class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countL = {}
        for n in nums:
            countL[n] = countL.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in countL.items():
            buckets[freq].append(num)

        res = []
        for freq in range(len(nums), 0, -1):
            for n in buckets[freq]:
                res.append(n)
                if len(res) == k:
                    return res
        return res  
