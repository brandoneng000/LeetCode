from typing import List

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        high_quality = -float('inf')
        radius_sq = radius * radius

        for x in range(51):
            for y in range(51):
                val = 0

                for tower_x, tower_y, quality in towers:
                    dist = (x - tower_x) ** 2 + (y - tower_y) ** 2
                    if dist <= radius_sq:
                        val += quality // (1 + dist ** 0.5)
                
                    if val > high_quality:
                        res = [x, y]
                        high_quality = val
        
        return res
                    

        
def main():
    sol = Solution()
    print(sol.bestCoordinate(towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2))
    print(sol.bestCoordinate(towers = [[23,11,21]], radius = 9))
    print(sol.bestCoordinate(towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2))

if __name__ == '__main__':
    main()