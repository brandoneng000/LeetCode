from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance_two_points(p1: List[int], p2: List[int]):
            return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        
        distance = []
        temp = [p1, p2, p3, p4]
        for i in range(len(temp)):
            for j in range(i + 1, len(temp)):
                distance.append(distance_two_points(temp[i], temp[j]))
        
        if distance.count(min(distance)) == 4 and distance.count(max(distance)) == 2:
            return True
        
        return False

def main():
    sol = Solution()
    print(sol.validSquare([0, 0], [13, 0], [5, 12], [18, 12]))
    print(sol.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))
    print(sol.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]))
    print(sol.validSquare(p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]))

if __name__ == '__main__':
    main()