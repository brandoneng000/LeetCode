from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n - 1 <= 0
            else:
                return n <= 0

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        for index in range(1, len(flowerbed) - 1):
            if n == 0:
                return True

            if flowerbed[index - 1] == 0 and flowerbed[index] == 0 and flowerbed[index + 1] == 0:
                flowerbed[index] = 1
                n -= 1
        
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            n -= 1

        return n <= 0


def main():
    sol = Solution()
    print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
    print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
    print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,0,0,1], n = 2))
    print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1,0,0], n = 2))

if __name__ == '__main__':
    main()