class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_obj = self.freq_calc(s)
        t_obj = self.freq_calc(t)
        if len(s) == len(t):
            for key in s_obj:
                if key in t_obj and s_obj[key] == t_obj[key]:
                    continue
                else:
                    return False
            return True
        
        return False
            

    def freq_calc(self,word):
        obj = {}
        for letter in word:
            if letter in obj:
                obj[letter] += 1
            else:
                obj[letter] = 0
        return obj