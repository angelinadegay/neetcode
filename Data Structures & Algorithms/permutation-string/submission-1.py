class Solution:


    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_f = self.find_freq(s1)
        window_freq = self.find_freq(s2[:len(s1)])

        if s1_f == window_freq:
            return True
        
        for i in range(len(s1), len(s2)):
            left = s2[i - len(s1)]
            window_freq[ord(left) - ord('a')] -= 1

            right = s2[i]
            window_freq[ord(right) - ord('a')] += 1

            if window_freq == s1_f:
                return True
        return False

    def find_freq(self, s):
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            return freq    




