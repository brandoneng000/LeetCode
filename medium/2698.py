class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check_partition(num: int, target: int):
            if target < 0 or num < target:
                return False
            
            if num == target:
                return True
            
            return (
                check_partition(num // 10, target - num % 10) 
                or check_partition(num // 100, target - num % 100)
                or check_partition(num // 1000, target - num % 1000)
            )
        
        res = 0

        for num in range(1, n + 1):
            square_num = num * num

            if check_partition(square_num, num):
                res += square_num
        
        return res


    # def punishmentNumber(self, n: int) -> int:
    #     def check_punish(index: int, start: str, goal: int):
    #         if index == len(start):
    #             return goal == 0
    #         if goal < 0:
    #             return False
            
    #         for i in range(index, len(start)):
    #             x = start[index: i + 1]
    #             y = int(x)

    #             if check_punish(i + 1, start, goal - y):
    #                 return True
            
    #         return False
        
    #     res = 0

    #     for i in range(1, n + 1):
    #         x = i * i
    #         num = str(x)
            
    #         if check_punish(0, num, i):
    #             res += x
        
    #     return res

        
def main():
    sol = Solution()
    print(sol.punishmentNumber(10))
    print(sol.punishmentNumber(37))

if __name__ == '__main__':
    main()