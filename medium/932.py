from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        cache = { 1:[1] }

        def helper(n: int):
            if n not in cache:
                odds = helper((n + 1) // 2)
                evens = helper(n // 2)
                cache[n] = [2 * val - 1 for val in odds] + [2 * val for val in evens]
            return cache[n]

        return helper(n)

def main():
    sol = Solution()
    print(sol.beautifulArray(4))
    print(sol.beautifulArray(5))

if __name__ == '__main__':
    main()