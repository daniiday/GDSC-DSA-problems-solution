class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        if x < 0:
            rev = -rev
        if rev > (2**31)-1 or rev < (-2)**31:
            return 0
        return rev
