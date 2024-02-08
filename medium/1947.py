from typing import List
from collections import defaultdict

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def get_score(student: List[int], mentor: List[int]):
            return sum(student[i] == mentor[i] for i in range(n))
        
        def dp(i: int, mask: int):
            if i >= m:
                return 0
            
            if (i, mask) in cache:
                return cache[(i, mask)]

            res = -float('inf')

            for j in range(m):
                if (mask >> j) & 1 == 1:
                    continue

                mask = mask | (1 << j)
                cur_score = get_score(students[i], mentors[j])
                next_score = dp(i + 1, mask)
                res = max(res, cur_score + next_score)
                mask = mask ^ (1 << j)
            
            cache[(i, mask)] = res
            return res

        m, n = len(students), len(students[0])
        cache = defaultdict(int)

        return dp(0, 0)
        
def main():
    sol = Solution()
    print(sol.maxCompatibilitySum(students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]))
    print(sol.maxCompatibilitySum(students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]))

if __name__ == '__main__':
    main()