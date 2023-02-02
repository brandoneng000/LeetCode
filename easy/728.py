from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            temp = num
            while temp > 0:
               remainder = temp % 10
               temp //= 10
               if remainder == 0:
                   break
               elif num % remainder != 0:
                   break
               elif temp == 0:
                    result.append(num)
        
        return result


def main():
    sol = Solution()
    print(sol.selfDividingNumbers(1, 22))
    print(sol.selfDividingNumbers(47, 85))

if __name__ == '__main__':
    main()