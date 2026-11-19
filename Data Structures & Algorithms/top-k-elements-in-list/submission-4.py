class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        freq_array = [[] for i in range(len(nums))]

        for key, value in count.items():
            freq_array[value-1].append(key)

        result = []
        for v in reversed(freq_array):
            if v:
                result.extend(v)
            if k == len(result):
                return result

        