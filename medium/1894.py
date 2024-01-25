from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk = sum(chalk)
        k %= total_chalk

        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c
        
def main():
    sol = Solution()
    print(sol.chalkReplacer(chalk = [5,1,5], k = 22))
    print(sol.chalkReplacer(chalk = [3,4,1,2], k = 25))

if __name__ == '__main__':
    main()