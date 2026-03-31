class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        mySet = set()
        
        for right in range(len(s)):
            while s[right] in mySet:
                mySet.remove(s[left])
                left += 1
            window_size = (right - left) + 1
            longest = max(longest, window_size)
            mySet.add(s[right])

        return longest
            
