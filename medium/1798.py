from typing import List

class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        res = 1

        for c in sorted(coins):
            if c > res:
                break
            res += c
        
        return res
        
def main():
    sol = Solution()
    print(sol.getMaximumConsecutive([1,3]))
    print(sol.getMaximumConsecutive([1,1,1,4]))
    print(sol.getMaximumConsecutive([1,4,10,3,1]))

if __name__ == '__main__':
    main()