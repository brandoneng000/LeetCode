from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def cars_repaired(time: int):
            cars = 0

            for r in ranks:
                cars += int((time // r) ** 0.5)
            
            return cars

        left, right = 1, max(ranks) * cars * cars

        while left < right:
            middle = (left + right) // 2

            if cars_repaired(middle) >= cars:
                right = middle
            else:
                left = middle + 1
        
        return left

        
def main():
    sol = Solution()
    print(sol.repairCars(ranks = [4,2,3,1], cars = 10))
    print(sol.repairCars(ranks = [5,1,8], cars = 6))

if __name__ == '__main__':
    main()