from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        prev = [0] * (n + 1)
        post = [0] * (n + 1)

        for i in range(1, n):
            if security[i] <= security[i - 1]:
                prev[i] = prev[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                post[i] = post[i + 1] + 1
            
        res = []

        for i in range(time, n - time):
            if prev[i] >= time and post[i] >= time:
                res.append(i)
        
        return res

        

def main():
    sol = Solution()
    print(sol.goodDaysToRobBank(security = [1,2,3,4], time = 1))
    print(sol.goodDaysToRobBank(security = [5,3,3,3,5,6,2], time = 2))
    print(sol.goodDaysToRobBank(security = [1,1,1,1,1], time = 0))
    print(sol.goodDaysToRobBank(security = [1,2,3,4,5,6], time = 2))

if __name__ == '__main__':
    main()