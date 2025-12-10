from typing import List
from math import factorial

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if complexity[0] >= min(complexity[1:]):
            return 0
        
        mod = 1_000_000_007
        
        return factorial(len(complexity) - 1) % mod

        
def main():
    sol = Solution()
    print(sol.countPermutations([1,2,3]))
    print(sol.countPermutations([3,3,3,4,4,4]))

if __name__ == '__main__':
    main()