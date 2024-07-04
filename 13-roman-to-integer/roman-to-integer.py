class Solution:
    def romanToInt(self, s: str) -> int:
        rtoa = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        for i in range(len(s)):
            if i > 0 and rtoa[s[i]] > rtoa[s[i - 1]]:
                res += rtoa[s[i]] - 2 * rtoa[s[i - 1]]
            else:
                res += rtoa[s[i]]
        return res