class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    xy += 1
                else:
                    yx += 1
        
        if (xy + yx) % 2 == 1:
            return -1
        
        res = xy // 2 + yx // 2
        if xy % 2 == 1:
            res += 2
        
        return res
        

def main():
    sol = Solution()
    print(sol.minimumSwap(s1 = "xx", s2 = "yy"))
    print(sol.minimumSwap(s1 = "xy", s2 = "yx"))
    print(sol.minimumSwap(s1 = "xx", s2 = "xy"))

if __name__ == '__main__':
    main()