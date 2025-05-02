class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        force = [0] * n

        f = 0

        for i in range(n):
            if dominoes[i] == 'R':
                f = n
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f - 1, 0)
            
            force[i] += f
        
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                f = n
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f - 1, 0)

            force[i] -= f
        
        res = []

        for f in force:
            if f == 0:
                res.append('.')
            elif f > 0:
                res.append('R')
            else:
                res.append('L')
        
        return ''.join(res)


    # def pushDominoes(self, dominoes: str) -> str:
    #     dominoes_list = list(dominoes)

    #     while True:
    #         temp = dominoes_list.copy()
    #         for i in range(len(dominoes_list) - 2, -1, -1):
    #             if dominoes_list[i] == '.' and dominoes_list[i + 1] == 'L':
    #                 if i > 0 and dominoes_list[i - 1] == 'R':
    #                     pass
    #                 else:
    #                     temp[i] = 'L'
    #         for i in range(1, len(dominoes_list)):
    #             if dominoes_list[i] == '.' and dominoes_list[i - 1] == 'R':
    #                 if i < len(dominoes_list) - 1 and dominoes_list[i + 1] == 'L':
    #                     pass
    #                 else:
    #                     temp[i] = 'R'
    #         if temp == dominoes_list:
    #             return "".join(dominoes_list)
    #         dominoes_list = temp

def main():
    sol = Solution()
    print(sol.pushDominoes("RR.L"))
    print(sol.pushDominoes(".L.R...LR..L.."))

if __name__ == '__main__':
    main()