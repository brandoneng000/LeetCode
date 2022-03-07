class Solution:
    def checkRecord(self, s: str) -> bool:
        return not (s.count('A') >= 2 or "LLL" in s)
        # from typing import Counter 
        # count = Counter(s)
        # return not (count['A'] >= 2 or "LLL" in s)

def main():
    sol = Solution()
    print(sol.checkRecord("PPALLP"))
    print(sol.checkRecord("PPAALLP"))
    print(sol.checkRecord("PPALLLP"))

if __name__ == '__main__':
    main()