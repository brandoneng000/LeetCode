from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        res = 0
        water = capacity

        for i in range(n):
            if water >= plants[i]:
                res += 1
            else:
                res += (i * 2) + 1
                water = capacity
            
            water -= plants[i]
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.wateringPlants(plants = [2,2,3,3], capacity = 5))
    print(sol.wateringPlants(plants = [1,1,1,4,2,3], capacity = 4))
    print(sol.wateringPlants(plants = [7,7,7,7,7,7,7], capacity = 8))

if __name__ == '__main__':
    main()