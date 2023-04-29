from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        last_index = [0] * len(primes)
        multiply = primes.copy()
        for i in range(1, n):
            smallest = min(multiply)
            ugly[i] = smallest
            for j in range(len(primes)):
                if smallest == multiply[j]:
                    last_index[j] += 1
                    multiply[j] = primes[j] * ugly[last_index[j]]

        return ugly[-1]
        



def main():
    sol = Solution()
    print(sol.nthSuperUglyNumber(n = 12, primes = [2,7,13,19]))
    print(sol.nthSuperUglyNumber(n = 1, primes = [2,3,5]))

if __name__ == '__main__':
    main()