from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.res = 0
        changes = [0] * n

        def helper(index: int, count: int):
            if index == len(requests):
                for i in range(n):
                    if changes[i] != 0:
                        return
            
                self.res = max(self.res, count)
                return
            
            changes[requests[index][0]] -= 1
            changes[requests[index][1]] += 1
            helper(index + 1, count + 1)
            changes[requests[index][0]] += 1
            changes[requests[index][1]] -= 1
            helper(index + 1, count)
        
        helper(0, 0)
        return self.res


def main():
    sol = Solution()
    print(sol.maximumRequests(n = 3, requests = [[0,0],[1,1],[0,0],[2,0],[2,2],[1,1],[2,1],[0,1],[0,1]]))
    print(sol.maximumRequests(n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))
    print(sol.maximumRequests(n = 3, requests = [[0,0],[1,2],[2,1]]))
    print(sol.maximumRequests(n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]))

if __name__ == '__main__':
    main()