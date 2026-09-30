class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bal_dict = {}
        resp = []
        for i, val in enumerate(nums):
            bal = target - val
            if bal in bal_dict:
                return [bal_dict[bal], i]
            bal_dict[val] = i
        
        return resp
        
        