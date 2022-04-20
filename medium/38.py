class Solution:
    def countAndSay(self, n: int) -> str:
        def countNums(num: str) -> str:
            num += "A"
            res = []
            cur = num[0]
            count = 0
            for digit in num:
                if cur == digit:
                    count += 1
                else:
                    res.append(str(count))
                    res.append(cur)
                    cur = digit
                    count = 1
            
            return "".join(res)
        
        if n == 1:
            return "1"
        num = self.countAndSay(n - 1)
        return countNums(num)


def main():
    sol = Solution()
    print(sol.countAndSay(4))

if __name__ == '__main__':
    main()