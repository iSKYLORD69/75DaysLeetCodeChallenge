class Solution:
    def fib(self, n):

        if n == 0:
            return 0

        if n == 1:
            return 1

        first = 0
        second = 1

        for i in range(2, n + 1):
            current = first + second

            first = second
            second = current

        return second