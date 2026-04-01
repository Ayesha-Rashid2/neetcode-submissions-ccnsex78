class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return_list = [0] * (len(temperatures))
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_t, stack_i = stack.pop()
                return_list[stack_i] = i - stack_i

            stack.append((t, i))
        return return_list

        
        
        '''
        counter = 0
        return_list = []

        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    return_list.append(j - i)
                    break
            else:
                return_list.append(0)
        return return_list
        '''

        
        