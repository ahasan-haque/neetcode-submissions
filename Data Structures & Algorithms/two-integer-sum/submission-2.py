class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        residue_dict = dict()
        for idx, num in enumerate(nums):
            if target - num in residue_dict:
                return [residue_dict[target - num], idx]
            else:
                residue_dict[num] = idx
