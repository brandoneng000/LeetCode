from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for num in range(n):
            if str(num).count('0') == 0 and str(n - num).count('0') == 0:
                return [num, n - num]

def main():
    sol = Solution()
    print(sol.getNoZeroIntegers(2))
    print(sol.getNoZeroIntegers(11))
    print(sol.getNoZeroIntegers(1010))

if __name__ == '__main__':
    main()