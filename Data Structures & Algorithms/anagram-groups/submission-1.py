
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap={}
        hlist=[]
        for s in  strs:
            if tuple(sorted(s)) not in hmap:
                hmap[tuple(sorted(s))]=[s]
            else:
                hmap[tuple(sorted(s))].append(s)
        for value in hmap.values():
            hlist.append(value)
        return hlist
            