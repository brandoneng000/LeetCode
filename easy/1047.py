class Solution:
    def removeDuplicates(self, s: str) -> str:
        from collections import deque

        stack = deque()

        for letter in s:
            if stack and letter == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)

        # stack = deque()
        # last_letter = ""

        # for letter in s:
        #     stack.append(letter)
        #     if last_letter == stack[-1]:
        #         while stack and last_letter == stack[-1]:
        #             last_letter = stack.pop()
        #         if stack:
        #             last_letter = stack[-1]
        #         else:
        #             last_letter = ""
        #     else:
        #         last_letter = letter

        # return "".join(stack)
        

def main():
    sol = Solution()
    print(sol.removeDuplicates("abbaca"))
    print(sol.removeDuplicates("azxxzy"))

if __name__ == '__main__':
    main()