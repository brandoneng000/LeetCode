class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        stack = []
        res = 0
        cur_max = 0
        clear_stack = False

        for bit in s:
            if bit == '0':
                if clear_stack:
                    stack.clear()
                    cur_max = 0
                    clear_stack = False
                stack.append(bit)
            else:
                clear_stack = True
                if stack:
                    stack.pop()
                    cur_max += 2
                    res = max(res, cur_max)
        
        return res



def main():
    sol = Solution()
    print(sol.findTheLongestBalancedSubstring("01000111"))
    print(sol.findTheLongestBalancedSubstring("00111"))
    print(sol.findTheLongestBalancedSubstring("111"))

if __name__ == '__main__':
    main()