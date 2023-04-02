from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = 0
        taxed = 0

        for upper, percent in brackets:
            earned = min(income - taxed, upper - taxed)
            taxed += earned
            res += earned * percent / 100
        
        return res
        

def main():
    sol = Solution()
    print(sol.calculateTax(brackets = [[3,50],[7,10],[12,25]], income = 10))
    print(sol.calculateTax(brackets = [[1,0],[4,25],[5,50]], income = 2))
    print(sol.calculateTax(brackets = [[2,50]], income = 0))

if __name__ == '__main__':
    main()