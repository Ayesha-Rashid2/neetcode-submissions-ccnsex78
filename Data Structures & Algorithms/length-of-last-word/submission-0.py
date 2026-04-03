class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        test = s.split()
        return len(test[-1])