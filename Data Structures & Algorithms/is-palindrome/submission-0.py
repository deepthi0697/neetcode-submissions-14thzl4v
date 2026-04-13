class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(ch  for ch in s.lower() if ch.isalnum()) 
        return string.lower() == string.lower()[::-1]