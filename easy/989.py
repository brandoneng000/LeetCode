from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = int(''.join([str(digit) for digit in num]))
        return [int(digit) for digit in list(str(num + k))]
    
def main():
    sol = Solution()
    print(sol.addToArrayForm(num = [1,2,0,0], k = 34))
    print(sol.addToArrayForm(num = [2,7,4], k = 181))
    print(sol.addToArrayForm(num = [2,1,5], k = 806))

if __name__ == '__main__':
    main()