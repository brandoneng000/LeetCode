from typing import List

class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        n = len(maximumHeight)
        maximumHeight.sort(reverse=True)
        res = 0
        cur = maximumHeight[0]

        for i in range(n):
            cur = min(cur, maximumHeight[i])

            if cur <= 0:
                return -1
            
            res += cur
            cur -= 1
        
        return res

        
def main():
    sol = Solution()
    print(sol.maximumTotalSum([2,3,4,3]))
    print(sol.maximumTotalSum([15,10]))
    print(sol.maximumTotalSum([2,2,1]))

if __name__ == '__main__':
    main()