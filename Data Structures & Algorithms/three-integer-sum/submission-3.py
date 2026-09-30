# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         arr_len = len(nums)
#         nums.sort()
        
#         for i, n in enumerate(nums):
#             diff = 0 - n
#             start = i + 1
#             end = arr_len - 1

#             if i != 0 and nums[i] == nums[i - 1]:
#                 continue
            
#             while start < end:
#                 current_sum = nums[start] + nums[end]

#                 if current_sum == diff:
#                     res.append([n, nums[start], nums[end]])
#                     start += 1
#                     end -= 1

#                 elif current_sum > diff:
#                     end -= 1

#                 else:
#                     start += 1

        
#         return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr_len = len(nums)
        nums.sort()

        for i, n in enumerate(nums):

            if i != 0 and nums[i] == nums[i - 1]:
                continue

            diff = 0 - n
            start = i + 1
            end = arr_len - 1

            while start < end:

                current_sum = nums[start] + nums[end]

                if current_sum == diff:
                    res.append([n, nums[start], nums[end]])

                    start += 1
                    end -= 1

                    # Skip duplicate values
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1

                elif current_sum > diff:
                    end -= 1

                else:
                    start += 1

        return res
        