class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_pointer = 0
        word2_pointer = 0
        res = ""



        while word1_pointer < len(word1) and word2_pointer < len(word2):
            res += word1[word1_pointer]
            res += word2[word2_pointer]
            word1_pointer += 1
            word2_pointer += 1
            
        while word1_pointer < len(word1):
            res += word1[word1_pointer]
            word1_pointer += 1
        while word2_pointer < len(word2):
            res += word2[word2_pointer]
            word2_pointer += 1

            
        return res

        