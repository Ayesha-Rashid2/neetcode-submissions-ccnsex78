class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0
        
        if len(s) > len(t):
            return False

        while len(s) > s_pointer and len(t) > t_pointer:
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            else:
                t_pointer += 1

        if s_pointer == len(s):
            return True
        return False



        

        
        