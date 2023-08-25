from typing import List

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        rest = []

        for r in restaurants:
            if veganFriendly == 1 and r[2] == 0:
                continue

            if r[3] <= maxPrice and r[4] <= maxDistance:
                rest.append(r.copy())
        
        rest.sort(key=lambda x: (x[1], x[0]), reverse=True)
        
        return [r[0] for r in rest]

def main():
    sol = Solution()
    print(sol.filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10))
    print(sol.filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10))
    print(sol.filterRestaurants(restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3))

if __name__ == '__main__':
    main()