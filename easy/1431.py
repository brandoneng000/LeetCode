from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candy_kid = max(candies)

        for index in range(len(candies)):
            candies[index] = candies[index] + extraCandies >= candy_kid
        
        return candies

def main():
    sol = Solution()
    print(sol.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
    print(sol.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))
    print(sol.kidsWithCandies(candies = [12,1,12], extraCandies = 10))

if __name__ == '__main__':
    main()