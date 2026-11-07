class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = defaultdict(list)
        for s in strs:
            alp =''.join(sorted(s))
            new_dict[alp].append(s)
        return list(new_dict.values())