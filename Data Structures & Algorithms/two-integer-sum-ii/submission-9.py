class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        res = []

        while start < end:
            # if numbers[start] > target:
            #     break

            diff = target - numbers[start]

            # print(diff)
            # print(numbers[end])
            # print(numbers[end] > target)
            if numbers[end] > diff:
                end = end - 1
            elif numbers[end] == diff:
                return [start+1, end+1]
            else:
                start = start + 1

        return res

        
        