class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        counter = 0
        mySet = set()
        
        for right in range(len(s)):
            while s[right] in mySet:
                mySet.remove(s[left])
                left += 1
        
            w = (right - left) + 1
            counter = max(counter, w)
            mySet.add(s[right])   
        
        return counter
        