class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            word_sorted = tuple(sorted(word))
            if word_sorted not in groups:
                groups[word_sorted] = []

            groups[word_sorted].append(word)
        return list(groups.values())
