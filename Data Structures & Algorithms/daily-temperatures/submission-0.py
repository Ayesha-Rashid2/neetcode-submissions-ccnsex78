class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
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

        
        