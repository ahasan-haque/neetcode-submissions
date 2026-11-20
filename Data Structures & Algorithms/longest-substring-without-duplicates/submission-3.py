class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        longest_substr = 0
        reserve = set()

        while r < len(s):
            while s[r] in reserve:
                reserve.remove(s[l])
                l += 1
            reserve.add(s[r])
            r += 1

            longest_substr = max(longest_substr, r - l)
        
        return longest_substr




