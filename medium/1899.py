from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target
        first = set()
        second = set()
        third = set()

        for i, (a, b, c) in enumerate(triplets):
            if a == x and b <= y and c <= z:
                first.add(i)
            
            if a <= x and b == y and c <= z:
                second.add(i)
            
            if a <= x and b <= y and c == z:
                third.add(i)
        
        return bool(first and second and third)

        
def main():
    sol = Solution()
    print(sol.mergeTriplets(triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]))
    print(sol.mergeTriplets(triplets = [[3,4,5],[4,5,6]], target = [3,2,5]))
    print(sol.mergeTriplets(triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]))

if __name__ == '__main__':
    main()