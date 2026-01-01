from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(str(d) for d in digits)) + 1
        return [int(digit) for digit in str(num)]
        
def main():
    sol = Solution()
    print(sol.plusOne([1,2,3]))
    print(sol.plusOne([4,3,2,1]))
    print(sol.plusOne([9]))

if __name__ == '__main__':
    main()