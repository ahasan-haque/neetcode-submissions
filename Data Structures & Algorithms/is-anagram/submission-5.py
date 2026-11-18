class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = dict()
        for a,b in zip(s, t):
            counter[a] = counter.setdefault(a, 0) + 1
            counter[b] = counter.setdefault(b, 0) - 1
        for v in counter.values():
            if v != 0:
                return False
        return True


        