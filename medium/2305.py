from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        n = len(cookies)

        def helper(index, zero_count):
            if n - index < zero_count:
                return float('inf')
            
            if index == n:
                return max(children)
            
            res = float('inf')

            for i in range(k):
                zero_count -= int(children[i] == 0)
                children[i] += cookies[index]

                res = min(res, helper(index + 1, zero_count))

                children[i] -= cookies[index]
                zero_count += int(children[i] == 0)
            
            return res
        
        return helper(0, k)

    # def distributeCookies(self, cookies: List[int], k: int) -> int:
    #     if len(cookies) <= k:
    #         return max(cookies)

    #     children = [0] * k
    #     self.res = float('inf')
    #     cookies.sort()

    #     def helper(children: List[int], index: int):
    #         if sum(children) == sum(cookies):
    #             self.res = min(self.res, max(children))
    #             return
            
    #         for i in range(index, len(cookies)):
    #             for j in range(len(children)):
    #                 children[j] += cookies[i]
    #                 helper(children, i + 1)
    #                 children[j] -= cookies[i]
        
    #     helper(children, 0)
    #     return self.res

def main():
    sol = Solution()
    print(sol.distributeCookies(cookies = [8,15,10,20,8], k = 2))
    print(sol.distributeCookies(cookies = [6,1,3,2,2,4,1,2], k = 3))

if __name__ == '__main__':
    main()