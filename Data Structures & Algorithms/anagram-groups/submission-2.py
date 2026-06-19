
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap=defaultdict(list)
        hlist=[]
        for s in  strs:
            
            hmap[tuple(sorted(s))].append(s)
        for value in hmap.values():
            hlist.append(value)
        return hlist
            