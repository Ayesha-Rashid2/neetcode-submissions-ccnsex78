class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_length = float('inf')  # start high
        i = 0

        for s in strs:
            if len(s) < min_length:  # find the minimum
                min_length = len(s)

        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1

        return strs[0][:i]