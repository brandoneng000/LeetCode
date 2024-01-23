class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == '-':
            x_str = str(x)

            for i in range(1, len(n)):
                if n[i] > x_str:
                    break
            else:
                i += 1
            
            return n[:i] + x_str + n[i:]
        else:
            x_str = str(x)
            for i in range(len(n)):
                if n[i] < x_str:
                    break
            else:
                i += 1
            
            return n[:i] + x_str + n[i:]
        
def main():
    sol = Solution()
    print(sol.maxValue(n = "-648468153646", x = 5))
    print(sol.maxValue(n = "-132", x = 3))
    print(sol.maxValue(n = "99", x = 9))
    print(sol.maxValue(n = "-13", x = 2))
    print(sol.maxValue(n = "13", x = 2))

if __name__ == '__main__':
    main()