from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [stones[0]]

        for i in range(1, n):
            prefix.append(prefix[-1] + stones[i])

        f = [0] * n
        f[-1] = prefix[-1]

        for i in range(n - 2, 0, -1):
            f[i] = max(f[i + 1], prefix[i] - f[i + 1])

        return f[1]

def main():
    sol = Solution()
    print(sol.stoneGameVIII([-1,2,-3,4,-5]))
    print(sol.stoneGameVIII([7,-6,5,10,5,-2,-6]))
    print(sol.stoneGameVIII([-10,-12]))

if __name__ == '__main__':
    main()