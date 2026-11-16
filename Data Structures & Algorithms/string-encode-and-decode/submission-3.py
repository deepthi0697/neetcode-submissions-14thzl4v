class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            delim = s.find('#',i)
            length = int(s[i:delim])
            res.append(s[delim + 1 : delim + 1 + length])
            i = delim+1+length
        return res