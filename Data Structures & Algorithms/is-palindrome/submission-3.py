class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        m=[]
        for i in s:
            if i.isalnum():
                m.append(i.lower())
        
        n=[]
        for i in range(len(m)-1,-1,-1):
            n.append(m[i])
        
        return m==n

        