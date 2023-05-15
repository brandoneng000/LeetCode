from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        
        matchstick_len = total_length // 4
        matchsticks.sort(reverse=True)
        sums = [0] * 4

        def dfs(index):
            if index == len(matchsticks):
                return sums[0] == sums[1] == sums[2] == matchstick_len
            
            for i in range(4):
                if sums[i] + matchsticks[index] <= matchstick_len:
                    sums[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sums[i] -= matchsticks[index]
            return False
        
        return dfs(0)
        

def main():
    sol = Solution()
    print(sol.makesquare([1,1,2,2,2]))
    print(sol.makesquare([3,3,3,3,4]))

if __name__ == '__main__':
    main()