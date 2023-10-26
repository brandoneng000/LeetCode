from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        res = 0
        cur_color = ""
        cur_time = float('inf')

        for i in range(n):
            if colors[i] == cur_color:
                if cur_time > neededTime[i]:
                    res += neededTime[i]
                else:
                    res += cur_time
                    cur_time = neededTime[i]
            else:
                cur_color = colors[i]
                cur_time = neededTime[i]
        
        return res

        
def main():
    sol = Solution()
    print(sol.minCost(colors = "abaac", neededTime = [1,2,3,4,5]))
    print(sol.minCost(colors = "abc", neededTime = [1,2,3]))
    print(sol.minCost(colors = "aabaa", neededTime = [1,2,3,4,1]))

if __name__ == '__main__':
    main()