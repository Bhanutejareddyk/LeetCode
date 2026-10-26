class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = s.lower()
        left=0
        right=len(ss)-1
        while left<right:
            if not ss[left].isalnum():
                left += 1
            elif not ss[right].isalnum():
                right -= 1
            elif ss[left] != ss[right]:
                return False
            else:
                left += 1
                right -= 1 
        return True               
        