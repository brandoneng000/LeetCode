class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []

        while a or b:
            if res[-2:] == ['a', 'a']:
                res.append('b')
                b -= 1
            elif res[-2:] == ['b', 'b']:
                res.append('a')
                a -= 1
            elif a > b:
                res.append('a')
                a -= 1
            else:
                res.append('b')
                b -= 1
        
        return "".join(res)
    # def strWithout3a3b(self, a: int, b: int) -> str:
    #     self.res = []

    #     def helper(a: int, b: int):
    #         if a < 3 and b < 3:
    #             if not self.res or self.res[-1] == 'a':
    #                 self.res.extend(['b'] * b)
    #                 self.res.extend(['a'] * a)
    #             else:
    #                 self.res.extend(['a'] * a)
    #                 self.res.extend(['b'] * b)
    #         elif a > b:
    #             self.res.append('a')
    #             self.res.append('a')
    #             self.res.append('b')
    #             helper(a - 2, b - 1)
    #         elif b > a:
    #             self.res.append('b')
    #             self.res.append('b')
    #             self.res.append('a')
    #             helper(a - 1, b - 2)
    #         else:
    #             self.res.append('a')
    #             self.res.append('b')
    #             helper(a - 1, b - 1)
        
    #     helper(a, b)
    #     return "".join(self.res)
        


def main():
    sol = Solution()
    print(sol.strWithout3a3b(a = 1, b = 2))
    print(sol.strWithout3a3b(a = 4, b = 1))

if __name__ == '__main__':
    main()