from typing import List

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        def check_fav_candy(fav_type, fav_day, daily):
            max_eat = candy_prefix[fav_type + 1] - 1
            min_eat = candy_prefix[fav_type] // daily

            return min_eat <= fav_day <= max_eat
        
        candy_prefix = [0]
        res = []

        for i in range(len(candiesCount)):
            candy_prefix.append(candy_prefix[-1] + candiesCount[i])
        
        for fav_type, fav_day, daily in queries:
            res.append(check_fav_candy(fav_type, fav_day, daily))
        
        return res
        
def main():
    sol = Solution()
    print(sol.canEat(candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]))
    print(sol.canEat(candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]))

if __name__ == '__main__':
    main()