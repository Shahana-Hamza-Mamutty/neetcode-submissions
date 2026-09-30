class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        # sorted_dict = sorted(count_dict.items(), key= lambda x: x[1], reverse=True)
        res = []
        # for key, val in sorted_dict:
        #     print(k)
        #     if k <= 0:
        #         break
            
        #     res.append(key)
        #     k = k - 1
        
        freq_array = [[] for _ in range(len(nums) + 1)]

        for key, val in count_dict.items():
            freq_array[val].append(key)

        for cnt in range(len(freq_array) - 1, 0, -1):
            for num in freq_array[cnt]:
                res.append(num)

                if len(res) == k:
                    return res
            
        return res

        