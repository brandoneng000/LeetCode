class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check_punish(index: int, start: str, goal: int):
            if index == len(start):
                return goal == 0
            if goal < 0:
                return False
            
            for i in range(index, len(start)):
                x = start[index: i + 1]
                y = int(x)

                if check_punish(i + 1, start, goal - y):
                    return True
            
            return False
        
        res = 0

        for i in range(1, n + 1):
            x = i * i
            num = str(x)
            
            if check_punish(0, num, i):
                res += x
        
        return res

        
def main():
    sol = Solution()
    print(sol.punishmentNumber(10))
    print(sol.punishmentNumber(37))

if __name__ == '__main__':
    main()