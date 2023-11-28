class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            return self.maximumGain(s[::-1], y, x)
        
        a = b = res = 0

        for letter in s:
            if letter == 'a':
                a += 1
            elif letter == 'b':
                if a:
                    res += x
                    a -= 1
                else:
                    b += 1
            else:
                res += min(a, b) * y
                a = b = 0
            
        return res + min(a, b) * y


        
def main():
    sol = Solution()
    print(sol.maximumGain(s = "cdbcbbaaabab", x = 4, y = 5))
    print(sol.maximumGain(s = "aabbaaxybbaabb", x = 5, y = 4))

if __name__ == '__main__':
    main()