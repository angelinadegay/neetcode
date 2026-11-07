class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = {}
        for s in strs:
            alp =''.join(sorted(s))
            if alp not in new_dict:
                new_dict[alp] = []
            new_dict[alp].append(s)
        return list(new_dict.values())