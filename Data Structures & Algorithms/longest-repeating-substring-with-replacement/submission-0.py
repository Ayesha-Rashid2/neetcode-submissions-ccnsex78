class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap = {}
        res = 0
        
        left = 0

        for right in range(len(s)):
            if s[right] in myMap:
                myMap[s[right]] += 1
            else:
                myMap[s[right]] = 1

            while (right - left + 1) - max(myMap.values()) > k:
                myMap[s[left]] -= 1
                left += 1


            res = max(res, right-left +1)
        return res
