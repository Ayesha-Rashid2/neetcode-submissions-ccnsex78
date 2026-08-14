class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        max_counter = 0
        left = 0

        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            my_set.add(s[right])
            max_counter = max(max_counter, right - left + 1)

        return max_counter





        