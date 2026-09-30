class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for _, val in enumerate(strs):
            s = ''.join(sorted(val))
            res[s].append(val)
            
        return list(res.values())
        