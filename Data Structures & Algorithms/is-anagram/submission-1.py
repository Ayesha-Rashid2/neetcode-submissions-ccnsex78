class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myMapS = {}
        myMapT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in myMapS:
                myMapS[s[i]] += 1
            else:
                myMapS[s[i]] = 1
            
            if t[i] in myMapT:
                myMapT[t[i]] += 1
            else:
                myMapT[t[i]] = 1

        if myMapS == myMapT:
            return True
        return False
        