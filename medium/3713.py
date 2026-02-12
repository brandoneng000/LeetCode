from typing import List

class Solution:
    def longestBalanced(self, s: str) -> int:
        def _check(count: List[int]):
            return len(set(count) - {0}) == 1

        n = len(s)
        res = 1

        for i in range(n):
            count = [0] * 26
            cur_max = 0

            for j in range(i, n):
                char = ord(s[j]) - ord('a')
                count[char] += 1

                if count[char] > cur_max:
                    cur_max = count[char]
                    
                    if _check(count):
                        res = max(res, j - i + 1)

                elif count[char] == cur_max and _check(count):
                    res = max(res, j - i + 1)
        
        return res

        
def main():
    sol = Solution()
    print(sol.longestBalanced("f"))
    print(sol.longestBalanced("abbac"))
    print(sol.longestBalanced("zzabccy"))
    print(sol.longestBalanced("aba"))

if __name__ == '__main__':
    main()