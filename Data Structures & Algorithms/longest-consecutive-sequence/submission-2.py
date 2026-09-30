class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        array_to_dict = Counter(nums)
        try:
            nums[0]
        except IndexError:
            return 0

        top = 1

        for n in nums:
            if not array_to_dict.get(n-1):
                a = n
                temp = 1
                while array_to_dict.get(a+1):
                    a = a + 1
                    temp = temp + 1
                    if top < temp:
                        top = temp
        return top


        

        