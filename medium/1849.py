from typing import List

class Solution:
    def splitString(self, s: str) -> bool:
        def helper(index: int, parts: int, prev_val: int):
            if index == n:
                return parts >= 2
            
            for i in range(index, n):
                num = int(s[index: i + 1])
                if prev_val == float('inf') or num == prev_val - 1:
                    if helper(i + 1, parts + 1, num):
                        return True
            
            return False
        
        n = len(s)
        return helper(0, 0, float('inf'))


def main():
    sol = Solution()
    print(sol.splitString("1234"))
    print(sol.splitString("050043"))
    print(sol.splitString("9080701"))

if __name__ == '__main__':
    main()