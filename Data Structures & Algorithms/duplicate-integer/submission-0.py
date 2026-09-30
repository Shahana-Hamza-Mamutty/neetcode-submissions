class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_list = {}
        for i, val in enumerate(nums):
            if count_list.get(val) is not None:
                return True
            count_list[val] = i
        
        return False

        