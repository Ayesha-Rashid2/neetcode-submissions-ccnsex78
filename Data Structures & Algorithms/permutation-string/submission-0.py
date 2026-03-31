class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = {}
        s2_map = {}

        for i, num in enumerate(s1):
            if num in s1_map:
                s1_map[num] += 1
            else:
                s1_map[num] = 1

            if s2[i] in s2_map:
                s2_map[s2[i]] += 1
            else:
                s2_map[s2[i]] = 1

        if s1_map == s2_map:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            if s2[right] in s2_map:
                s2_map[s2[right]] += 1
            else:
                s2_map[s2[right]] = 1

            s2_map[s2[left]] -= 1
            if s2_map[s2[left]] == 0:
                del s2_map[s2[left]]

            left += 1

            if s1_map == s2_map:
                return True

        return False