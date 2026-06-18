class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m={}
        n={}
        for i in s:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        for j in t:
            if j in n:
                n[j]+=1
            else:
                n[j]=1
        return m==n


        