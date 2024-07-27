from collections import deque

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res = 0
        q = deque()
        semi_rep = False

        for val in s:
            if q:
                if q[-1] == val and not semi_rep:
                    semi_rep = True
                elif q[-1] == val and semi_rep:
                    while q[0] != q[1]:
                        q.popleft()
                    q.popleft()
                
            q.append(val)
            res = max(res, len(q))
            
        return res
        
def main():
    sol = Solution()
    print(sol.longestSemiRepetitiveSubstring("52233"))
    print(sol.longestSemiRepetitiveSubstring("5494"))
    print(sol.longestSemiRepetitiveSubstring( "1111111"))

if __name__ == '__main__':
    main()