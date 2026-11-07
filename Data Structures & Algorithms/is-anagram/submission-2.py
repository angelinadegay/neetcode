class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        if len(s) != len(t):
            return False

        for l in s:
            count[l] = count.get(l, 0) + 1

        for l in t:
            if l not in count:
                return False
            count[l] -= 1

            if count[l] < 0:
                return False
        return True

        