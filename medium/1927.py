class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        question_left = left = 0
        question_right = right = 0

        for i in range(n // 2):
            if num[i].isdigit():
                left += int(num[i])
            else:
                question_left += 1
        
        for i in range(n // 2, n):
            if num[i].isdigit():
                right += int(num[i])
            else:
                question_right += 1
        
        num_diff = left - right
        q_diff = question_right - question_left

        return not (q_diff % 2 == 0 and q_diff // 2 * 9 == num_diff)
        
def main():
    sol = Solution()
    print(sol.sumGame("5023"))
    print(sol.sumGame("25??"))
    print(sol.sumGame("?3295???"))

if __name__ == '__main__':
    main()