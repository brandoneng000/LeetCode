from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        n = 32
        res = [0] * n

        for num in candidates:
            for i in range(n):
                res[i] += (num >> i) & 1

        return max(res)
    
def main():
    sol = Solution()
    print(sol.largestCombination([16,17,71,62,12,24,14]))
    print(sol.largestCombination([8,8]))

if __name__ == '__main__':
    main()