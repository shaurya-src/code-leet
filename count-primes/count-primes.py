class Solution:
    def countPrimes(self, n: int) -> int:
        not_prime = set()
        prime = set()
        for i in range(2, n):
            if i not in not_prime:
                prime.add(i)
                j = 1
                num = i*j
                while num < n:
                    not_prime.add(num)
                    j += 1
                    num = i*j
        print(prime)
        return len(prime)