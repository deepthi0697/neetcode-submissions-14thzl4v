class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        length = 0
        L = 0
        for R in range(len(s)):
            while s[R] in sub:
                sub.remove(s[L])
                L+=1
            sub.add(s[R])
            length = max(length, len(sub))
        return length