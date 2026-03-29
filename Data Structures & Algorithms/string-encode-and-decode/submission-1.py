class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str+= str(len(s)) + "#"+ s
        return new_str

    def decode(self, s: str) -> List[str]:
        return_string = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            return_string.append(s[j+1:j+1+length])
            i = j + 1 + length
        return return_string

