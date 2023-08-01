class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for letter in s:
            if not stack:
                stack.append((letter, 1))
            else:
                if letter == stack[-1][0]:
                    if stack[-1][1] < k - 1:
                        stack.append((letter, stack[-1][1] + 1))
                    else:
                        for _ in range(k - 1):
                            stack.pop()
                else:
                    stack.append((letter, 1))

        return "".join(letter for letter, count in stack)
    
def main():
    sol = Solution()
    print(sol.removeDuplicates(s = "abcd", k = 2))
    print(sol.removeDuplicates(s = "deeedbbcccbdaa", k = 3))
    print(sol.removeDuplicates(s = "pbbcggttciiippooaais", k = 2))

if __name__ == '__main__':
    main()