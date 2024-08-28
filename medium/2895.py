from typing import List

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        m, n = len(processorTime), len(tasks)
        tasks.sort(reverse=True)
        processorTime.sort()
        res = 0
        
        for i in range(m):
            index = i * 4

            for j in range(4):
                res = max(res, processorTime[i] + tasks[index + j])
        
        return res
        
def main():
    sol = Solution()
    print(sol.minProcessingTime(processorTime = [8,10], tasks = [2,2,3,1,8,7,4,5]))
    print(sol.minProcessingTime(processorTime = [10,20], tasks = [2,3,1,2,5,8,4,3]))

if __name__ == '__main__':
    main()