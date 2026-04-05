class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for str in strs[1:]:
            while str[:len(prefix)] != prefix:
                prefix = prefix[:-1]

                if not prefix:
                    return ''
        
        return prefix
        
        
        
        '''  O(s) time complexity where S is the sum of all characters and all the strings
        res = ""

        if not strs:
            return res

        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return res
            res += char
        
        
        return res
        '''