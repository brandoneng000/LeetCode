class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        question_left = left = 0
        question_right = right = 0

        for i in range(mid):
            if num[i] == '?':
                question_left += 1
            else:
                left += int(num[i])

        for i in range(mid, n):
            if num[i] == '?':
                question_right += 1
            else:
                right += int(num[i])
        
        num_diff = left - right
        q_diff = question_right - question_left

        return not (q_diff % 2 == 0 and q_diff // 2 * 9 == num_diff)

    
    # def sumGame(self, num: str) -> bool:
    #     n = len(num)
    #     mid = n // 2
    #     left = 0
    #     diff = 0
    #     q = 0

    #     for i in range(n):
    #         if num[i] == '?':
    #             q += 1

    #             if i < mid:
    #                 left += 1

    #         elif i < n // 2:
    #             diff += int(num[i])
    #         else:
    #             diff -= int(num[i])

    #     if q % 2:
    #         return True

    #     right = q - left

    #     return diff != 9 * (right - left) // 2

    # def sumGame(self, num: str) -> bool:
    #     n = len(num)
    #     question_left = left = 0
    #     question_right = right = 0

    #     for i in range(n // 2):
    #         if num[i].isdigit():
    #             left += int(num[i])
    #         else:
    #             question_left += 1
        
    #     for i in range(n // 2, n):
    #         if num[i].isdigit():
    #             right += int(num[i])
    #         else:
    #             question_right += 1
        
    #     num_diff = left - right
    #     q_diff = question_right - question_left

    #     return not (q_diff % 2 == 0 and q_diff // 2 * 9 == num_diff)
        
def main():
    sol = Solution()
    print(sol.sumGame("5023"))
    print(sol.sumGame("25??"))
    print(sol.sumGame("?3295???"))

if __name__ == '__main__':
    main()