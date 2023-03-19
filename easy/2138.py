from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = [s[i:i + k] for i in range(0, len(s), k)]
        if len(result[-1]) != k:
            result[-1] += fill * (k - len(result[-1]))
        return result
    
def main():
    sol = Solution()
    print(sol.divideString(s = "abcdefghi", k = 3, fill = "x"))
    print(sol.divideString(s = "abcdefghij", k = 3, fill = "x"))

if __name__ == '__main__':
    main()