class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        llist=[[] for i in range(len(nums)+1)]
        for i in nums:
            hmap[i]=1+hmap.get(i,0)
        for i,v in hmap.items():
            llist[v].append(i)
        res=[]
        for i in range(len(llist)-1,-1,-1):
            for j in llist[i]:
                res.append(j)
                if len(res)==k:
                    return res
        