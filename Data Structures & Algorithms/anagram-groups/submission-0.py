class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = self.creation(word)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        return list(groups.values())

    def creation(self, eachString):
        myMap = {}
        for s in eachString:
            if s in myMap:
                myMap[s] += 1
            else:
                myMap[s] = 1
        return tuple(sorted(myMap.items()))