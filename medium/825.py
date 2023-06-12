from typing import List
import collections

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def helper(x, y):
            return not (y <= 0.5 * x + 7 or y > x or y > 100 and x < 100)
        
        age_count = collections.Counter(ages)

        return sum(helper(x, y) * age_count[x] * (age_count[y] - (x == y)) for x in age_count for y in age_count)

def main():
    sol = Solution()
    print(sol.numFriendRequests([16,16]))
    print(sol.numFriendRequests([16,17,18]))
    print(sol.numFriendRequests([20,30,100,110,120]))

if __name__ == '__main__':
    main()