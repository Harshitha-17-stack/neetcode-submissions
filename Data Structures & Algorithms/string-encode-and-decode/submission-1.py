class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s+=str(st+"foenem")
        return s
    def decode(self, s: str) -> List[str]:
        return s.split('foenem')[:-1]