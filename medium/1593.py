from typing import List

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(s: str, used: set):
            res = 0

            if s:
                for i in range(1, len(s) + 1):
                    candidate = s[:i]
                    if candidate not in used:
                        used.add(candidate)
                        res = max(res, 1 + backtrack(s[i:], used))
                        used.remove(candidate)
            
            return res

        used = set()
        return backtrack(s, used)
        
def main():
    sol = Solution()
    print(sol.maxUniqueSplit("wwwzfvedwfvhsww"))
    print(sol.maxUniqueSplit("ababccc"))
    print(sol.maxUniqueSplit("aba"))
    print(sol.maxUniqueSplit("aa"))

if __name__ == '__main__':
    main()