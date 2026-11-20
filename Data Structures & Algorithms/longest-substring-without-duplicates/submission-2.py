class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        longest_substr = 0
        reserve = set()
        while r < len(s):
            if s[r] not in reserve:
                reserve.add(s[r])
                r += 1
            else:
                longest_substr = max(longest_substr, r-l)
                reserve.remove(s[l])
                l += 1

        return max(longest_substr, r-l)
        



