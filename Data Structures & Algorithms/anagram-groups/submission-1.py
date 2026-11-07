class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagr_map = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            anagr_map[key].append(s)

        return list(anagr_map.values())
        