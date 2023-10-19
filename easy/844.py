class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for c in s:
            if c == '#' and s_stack:
                s_stack.pop()
            elif c != '#':
                s_stack.append(c)
        
        for c in t:
            if c == '#' and t_stack:
                t_stack.pop()
            elif c != '#':
                t_stack.append(c)
        
        return s_stack == t_stack

    # def backspaceCompare(self, s: str, t: str) -> bool:
    #     new_s = ""
    #     new_t = ""
        
    #     for letter in s:
    #         if letter == '#' and len(new_s) > 0:
    #             new_s = new_s[:-1]
    #         elif letter != '#':
    #             new_s += letter

    #     for letter in t:
    #         if letter == '#' and len(new_t) > 0:
    #             new_t = new_t[:-1]
    #         elif letter != '#':
    #             new_t += letter

    #     return new_s == new_t

def main():
    sol = Solution()
    print(sol.backspaceCompare("y#fo##f", "y#f#o##f"))
    print(sol.backspaceCompare("ab#c", "ad#c"))
    print(sol.backspaceCompare("ab##", "c#d#"))
    print(sol.backspaceCompare("a#c", "b"))

if __name__ == '__main__':
    main()