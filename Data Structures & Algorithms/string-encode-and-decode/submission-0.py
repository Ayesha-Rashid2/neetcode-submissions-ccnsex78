class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ''
        for s in strs:
            new_str+= s + ',:'
        return new_str

    def decode(self, s: str) -> List[str]:
        return_list = s.split(",:")
        return_list.pop()
        return return_list

