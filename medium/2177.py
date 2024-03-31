from typing import List

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        
        val = num // 3
        return [val - 1, val, val + 1]
        
def main():
    sol = Solution()
    print(sol.sumOfThree(33))
    print(sol.sumOfThree(4))

if __name__ == '__main__':
    main()