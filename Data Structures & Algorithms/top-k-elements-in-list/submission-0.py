class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        return [i[0] for i in sorted(count.items(), key=lambda x: -x[1])][:k]


        