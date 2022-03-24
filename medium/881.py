from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        first = 0
        second = len(people) - 1
        
        while second >= 0 and people[second] >= limit:
            second -= 1
            boats += 1

        while first <= second:
            weight = people[first] + people[second]
            while first < second and weight > limit:
                second -= 1
                boats += 1
                weight = people[first] + people[second]
            first += 1
            second -= 1
            boats += 1
        
        return boats
        
def main():
    sol = Solution()
    print(sol.numRescueBoats([3, 3, 3, 3, 3], 3))
    print(sol.numRescueBoats([1,2], 3))
    print(sol.numRescueBoats([3,2,2,1], 3))
    print(sol.numRescueBoats([3,5,3,4], 5))
    print(sol.numRescueBoats([5, 1, 2, 4], 6))

if __name__ == '__main__':
    main()