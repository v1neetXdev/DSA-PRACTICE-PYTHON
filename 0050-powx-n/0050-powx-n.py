class Solution(object):
    def myPow(self, x, n):

        if n < 0:
            x = 1 / x
            n = -n

        total = 1

        while n > 0:

            if n % 2 == 1:
                total = total * x

            x = x * x
            n = n // 2

        return total
        