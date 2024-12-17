class Solution:
    def isHappy(self, n):
        while n >= 1:
            x = n
            n = 0
            while x > 0:
                n += (x % 10) ** 2
                x = x // 10
            if n == 1:
                return True
            if n == 4:
                return False
print(Solution().isHappy(1))