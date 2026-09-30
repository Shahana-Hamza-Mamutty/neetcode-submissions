class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp_stack = []

        for i, val in enumerate(temperatures):
            if i == 0:
                temp_stack.append(i)
                continue
            while temp_stack and temperatures[temp_stack[-1]] < val:
                popped = temp_stack.pop()
                result[popped] = i - popped
            
            temp_stack.append(i)
        
        return result

            
        
        