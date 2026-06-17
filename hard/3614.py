class Solution:
    def processStr(self, s: str, k: int) -> str:
        length = 0

        for ch in s:
            if ch == '*':
                if length:
                    length -= 1
            elif ch == '#':
                length *= 2
            elif ch == '%':
                pass
            else:
                length += 1

        if k + 1 > length:
            return '.'
        
        for ch in reversed(s):
            if ch == '*':
                length += 1
            elif ch == '#':
                if k + 1 > (length + 1) // 2:
                    k -= length // 2
                length = (length + 1) // 2
            elif ch == '%':
                k = length - k - 1
            else:
                if k + 1 == length:
                    return ch
                length -= 1

        return '.'
        
def main():
    sol = Solution()
    print(sol.processStr(s = "a#b%*", k = 1))
    print(sol.processStr(s = "cd%#*#", k = 3))
    print(sol.processStr(s = "z*#", k = 0))

if __name__ == '__main__':
    main()