class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        for idx, value in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx -1]:
                continue
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[left] + nums[right] + value
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([nums[left] , nums[right] , value])
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
        return result

        