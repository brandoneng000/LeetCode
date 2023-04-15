from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(start: int, res: List[str], cur: List[str]):
            if start >= len(s):
                res.append(cur.copy())
                return
            
            for end in range(start, len(s)):
                if is_palindrome(s[start: end + 1]):
                    cur.append(s[start: end + 1])
                    dfs(end + 1, res, cur)
                    cur.pop()
        
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        dfs(0, res, [])
        return res

    

def main():
    sol = Solution()
    print(sol.partition("aab"))
    print(sol.partition("a"))

if __name__ == '__main__':
    main()