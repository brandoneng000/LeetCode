from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n

        for index in range(1, n):
            if ratings[index] > ratings[index - 1]:
                candy[index] = candy[index - 1] + 1
        
        for index in range(n - 2, -1, -1):
            if ratings[index] > ratings[index + 1]:
                candy[index] = max(candy[index], candy[index + 1] + 1)
            
        return sum(candy)

def main():
    sol = Solution()
    print(sol.candy([29,51,87,87,72,12]))
    print(sol.candy([1,0,2]))
    print(sol.candy([1,2,2]))

if __name__ == '__main__':
    main()