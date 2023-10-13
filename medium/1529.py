class Solution:
    def minFlips(self, target: str) -> int:
        res = 0
        status = '0'

        for bit in target:
            if bit != status:
                res += 1
                status = '0' if status == '1' else '1'
        
        return res


    # def minFlips(self, target: str) -> int:
    #     ones = [[0]]
    #     res = 0

    #     for bit in target:
    #         if bit == '1':
    #             ones[-1][0] += 1
    #         else:
    #             ones.append([0])
        
    #     for count in ones:
    #         if count[0] > 0:
    #             res += 2
        
    #     if res == 0:
    #         return 0

    #     return res - 1 if target[-1] == '1' else res

def main():
    sol = Solution()
    print(sol.minFlips("10111"))
    print(sol.minFlips("101"))
    print(sol.minFlips("00000"))

if __name__ == '__main__':
    main()