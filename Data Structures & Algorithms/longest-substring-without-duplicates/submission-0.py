class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0

        letSet = set()


        while right < len(s):
            if s[right] in letSet:
                letSet.remove((s[left]))
                left += 1
        
    
            else:
                letSet.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
        return max_length
        