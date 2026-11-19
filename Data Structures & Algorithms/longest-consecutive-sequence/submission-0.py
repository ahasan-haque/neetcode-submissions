class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        unique_nums = set(nums)
        for num in nums:
            if num -1 in unique_nums:
                continue
            else:
                i = 1
                while num + i in unique_nums:
                    i += 1
                if i > max_length:
                    max_length = i
        return max_length
