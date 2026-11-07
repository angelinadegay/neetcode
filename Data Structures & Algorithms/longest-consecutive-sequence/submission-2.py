class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in check:
                count = 1
                current = n
            
                while (current + 1) in check:
                    count += 1
                    current += 1
                    
                longest = max(longest, count)
        return longest

        