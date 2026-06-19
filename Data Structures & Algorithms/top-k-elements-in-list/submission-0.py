class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m=Counter(nums).most_common(k)
        return [item for item,count in m]
