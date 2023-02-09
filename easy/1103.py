from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        person = 0
        candy = 1

        while candy < candies:
            result[person] += candy
            candies -= candy
            person += 1
            candy += 1
            if person == num_people:
                person = 0
            
        result[person] += candies
        return result

def main():
    sol = Solution()
    print(sol.distributeCandies(7, 4))
    print(sol.distributeCandies(10, 3))

if __name__ == '__main__':
    main()