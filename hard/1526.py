from typing import List

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        res = target[0]

        for i in range(1, n):
            res += max(target[i] - target[i - 1], 0)
        
        return res
        
def main():
    sol = Solution()
    print(sol.minNumberOperations([1,2,3,2,1]))
    print(sol.minNumberOperations([3,1,1,2]))
    print(sol.minNumberOperations([3,1,5,4,2]))

if __name__ == '__main__':
    main()