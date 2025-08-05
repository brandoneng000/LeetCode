from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        filled = [False] * n

        for f in fruits:
            for i in range(n):
                if not filled[i] and f <= baskets[i]:
                    filled[i] = True
                    break
        
        return n - sum(filled)
        
def main():
    sol = Solution()
    print(sol.numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4]))
    print(sol.numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7]))

if __name__ == '__main__':
    main()