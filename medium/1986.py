from typing import List

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        def helper(index: int):
            if len(subsets) >= self.res:
                return
            
            if index == n:
                self.res = min(self.res, len(subsets))
                return
            
            for i in range(len(subsets)):
                if subsets[i] + tasks[index] <= sessionTime:
                    subsets[i] += tasks[index]
                    helper(index + 1)
                    subsets[i] -= tasks[index]
            
            subsets.append(tasks[index])
            helper(index + 1)
            subsets.pop()

        n = len(tasks)
        subsets = []
        self.res = n
        helper(0)
        return self.res


        
def main():
    sol = Solution()
    print(sol.minSessions(tasks = [1,2,3], sessionTime = 3))
    print(sol.minSessions(tasks = [3,1,3,1,1], sessionTime = 8))
    print(sol.minSessions(tasks = [1,2,3,4,5], sessionTime = 15))

if __name__ == '__main__':
    main()