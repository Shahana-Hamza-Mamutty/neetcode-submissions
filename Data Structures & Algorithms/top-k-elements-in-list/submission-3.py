class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        sorted_dict = sorted(count_dict.items(), key= lambda x: x[1], reverse=True)
        res = []
        for key, val in sorted_dict:
            print(k)
            if k <= 0:
                break
            
            res.append(key)
            k = k - 1
            
            
        return res

        