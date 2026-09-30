class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        res = []

        while start < end:
            diff = target - numbers[start]
            if numbers[end] > diff:
                end = end - 1
            elif numbers[end] == diff:
                return [start+1, end+1]
            else:
                start = start + 1

        return res

        
        