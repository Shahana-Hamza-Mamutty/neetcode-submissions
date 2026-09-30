class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)
        for _, val in enumerate(strs):
            count_arr = [0] * 26
            for l in val:
                pos = ord(l) - ord("a")
                count_arr[pos] += 1
            key = tuple(count_arr)
            res[key].append(val)   
        
        return list(res.values())


        


        