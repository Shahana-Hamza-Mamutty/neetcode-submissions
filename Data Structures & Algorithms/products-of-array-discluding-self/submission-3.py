class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mux_arr = [1] * n
        rev_mux_arr = [1] * n
        res = []
        last_idx = len(nums) - 1

        for i, num in enumerate(nums):
            if i == 0:
                mux_arr[i] = num
            else:
                mux_arr[i] = (num * mux_arr[i-1])
        

        for i in range(last_idx, -1, -1):
            if i == last_idx:
                rev_mux_arr[i] = nums[i]
            else:
                rev_mux_arr[i] = nums[i] * rev_mux_arr[i+1]
        
        for i, n in enumerate(nums):
            if i == 0:
                res.append(rev_mux_arr[i+1])
            elif i == last_idx:
                res.append(mux_arr[i-1])
            else:
                res.append(mux_arr[i-1] * rev_mux_arr[i+1])
        
        return res

            
        

            


        