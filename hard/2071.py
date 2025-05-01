from typing import List
from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        left = 0
        right = min(len(tasks), len(workers))

        while left < right:
            middle = (left + right + 1) // 2
            used_pills = 0
            available_workers = workers[-middle:]
            can_assign = True

            for task in reversed(tasks[:middle]):
                if available_workers[-1] >= task:
                    available_workers.pop()
                else:
                    index = bisect_left(available_workers, task - strength)

                    if index == len(available_workers) or used_pills == pills:
                        can_assign = False
                        break
                    used_pills += 1
                    available_workers.pop(index)
            
            if can_assign:
                left = middle
            else:
                right = middle - 1
        
        return left

        
def main():
    sol = Solution()
    print(sol.maxTaskAssign(tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1))
    print(sol.maxTaskAssign(tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5))
    print(sol.maxTaskAssign(tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10))

if __name__ == '__main__':
    main()