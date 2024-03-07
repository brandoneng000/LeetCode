from typing import List
from collections import deque

class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        q = deque([start])
        visited = set()
        step = 0

        while q:
            size = len(q)

            for _ in range(size):
                cur = q.popleft()

                if cur == goal:
                    return step
                
                if cur > 1000 or cur < 0 or cur in visited:
                    continue
                
                visited.add(cur)
                for num in nums:
                    q.append(cur - num)
                    q.append(cur + num)
                    q.append(cur ^ num)

            step += 1

        return -1
        
def main():
    sol = Solution()
    print(sol.minimumOperations(nums = [2,4,12], start = 2, goal = 12))
    print(sol.minimumOperations(nums = [3,5,7], start = 0, goal = -4))
    print(sol.minimumOperations(nums = [2,8,16], start = 0, goal = 1))

if __name__ == '__main__':
    main()