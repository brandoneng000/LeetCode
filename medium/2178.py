from typing import List

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        res = []
        cur = 2

        if finalSum % 2 == 0:
            while cur <= finalSum:
                res.append(cur)
                finalSum -= cur
                cur += 2
            res[-1] += finalSum
        
        return res
        


        
def main():
    sol = Solution()
    print(sol.maximumEvenSplit(12))
    print(sol.maximumEvenSplit(7))
    print(sol.maximumEvenSplit(28))

if __name__ == '__main__':
    main()