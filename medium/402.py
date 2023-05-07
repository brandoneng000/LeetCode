from typing import List

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(num)
        stack = []

        for index in range(len(num)):
            while stack and k and stack[-1] > num[index]:
                stack.pop()
                k -= 1

            if stack or num[index] != '0':
                stack.append(num[index])

        if k:
            stack = stack[: -k]
        
        return ''.join(stack) or '0'

        
        

def main():
    sol = Solution()
    print(sol.removeKdigits(num = "1432219", k = 3))
    print(sol.removeKdigits(num = "10200", k = 1))
    print(sol.removeKdigits(num = "10", k = 2))

if __name__ == '__main__':
    main()