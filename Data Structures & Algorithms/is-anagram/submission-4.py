class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map_1 = {}
        hash_map_2 = {}

        for c in s:
            hash_map_1[c] = hash_map_1.get(c, 0) + 1
            
        for k in t:
            hash_map_2[k] = hash_map_2.get(k, 0) + 1

        if hash_map_2 == hash_map_1:
            return True

        else:
            return False
                