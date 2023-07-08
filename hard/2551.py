from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        splits = [0] * (n - 1)
        for i in range(n - 1):
            splits[i] = weights[i] + weights[i + 1]
        
        splits.sort()
        res = 0

        for i in range(k - 1):
            res += splits[n - 2 - i] - splits[i]
        
        return res

def main():
    sol = Solution()
    print(sol.putMarbles(weights = [1,3,5,1,5,2,3,5,7,8,1], k = 5))
    print(sol.putMarbles(weights = [1,3,5,1], k = 2))
    print(sol.putMarbles(weights = [1, 3], k = 2))

if __name__ == '__main__':
    main()