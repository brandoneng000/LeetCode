from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        amount = len(candyType) // 2
        candy = len(set(candyType))

        return min(amount, candy)

def main():
    sol = Solution()
    print(sol.distributeCandies([1,1,2,2,3,3]))
    print(sol.distributeCandies([1,1,2,3]))
    print(sol.distributeCandies([6,6,6,6]))

if __name__ == '__main__':
    main()