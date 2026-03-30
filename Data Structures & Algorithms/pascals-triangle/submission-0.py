class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return_list = []

        for i in range(numRows):
            sub_list = [1] * (i+1)
            num_valuesToChange = len(sub_list) - 2
            while num_valuesToChange >= 1:
                sub_list[num_valuesToChange] = return_list[i-1][num_valuesToChange] + return_list[i-1][num_valuesToChange-1]
                num_valuesToChange -= 1
            return_list.append(sub_list)
        return return_list