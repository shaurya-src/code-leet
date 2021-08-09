class Solution:
    def fib(self, n: int) -> int:
        cache = [0, 1, 1]
        if n < 0:
            return -1
        if 0 < n < 3:
            return cache [n]

        for i in range(3, n+1):
            cache.append(cache[i-2]+cache[i-1])

        return cache[n]