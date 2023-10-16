class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        n = len(s)
        shift = [0] * 26

        for i in range(n):
            diff = (ord(t[i]) - ord(s[i]))
            if diff < 0:
                diff += 26

            if diff > 0 and shift[diff] * 26 + diff > k:
                return False

            shift[diff] += 1
        
        return True

def main():
    sol = Solution()
    print(sol.canConvertString(s = "input", t = "ouput", k = 9))
    print(sol.canConvertString(s = "abc", t = "bcd", k = 10))
    print(sol.canConvertString(s = "aab", t = "bbb", k = 27))

if __name__ == '__main__':
    main()