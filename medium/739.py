from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        
        return res
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     res = [0] * len(temperatures)
    #     stack = []
        
    #     for i in range(len(temperatures) - 1, -1, -1):
    #         while stack and stack[-1][0] <= temperatures[i]:
    #             stack.pop()
    #         if stack:
    #             res[i] = stack[-1][1] - i
    #         stack.append((temperatures[i], i))
        
    #     return res


def main():
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(sol.dailyTemperatures([30,40,50,60]))
    print(sol.dailyTemperatures([30,60,90]))

if __name__ == '__main__':
    main()