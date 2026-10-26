class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = {}
        c2 = {}
        for ch in s:
            if ch not in c1:
                c1[ch]=0
            c1[ch]+=1
        for ch in t:
            if ch not in c2:
                c2[ch]=0
            c2[ch]+=1
        return c1 == c2                
        # if len(s) != len(t):
        #     return False
            
        # return Counter(s) == Counter(t)
        