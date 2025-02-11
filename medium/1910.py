class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, '', 1)
        
        return s

    # def removeOccurrences(self, s: str, part: str) -> str:
    #     return self.removeOccurrences(s.replace(part, '', 1), part) if part in s else s

    # def removeOccurrences(self, s: str, part: str) -> str:
    #     part_list = list(part)
    #     stack = []

    #     for letter in s:
    #         stack.append(letter)

    #         if stack[-len(part):] == part_list:
    #             for _ in range(len(part)):
    #                 stack.pop()
        
    #     return ''.join(stack)
        
def main():
    sol = Solution()
    print(sol.removeOccurrences(s = "aabababa", part = "aba"))
    print(sol.removeOccurrences(s = "daabcbaabcbc", part = "abc"))
    print(sol.removeOccurrences(s = "axxxxyyyyb", part = "xy"))

if __name__ == '__main__':
    main()