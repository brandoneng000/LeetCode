class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # stack = { 'L': 0, 'R': 0 }
        # res = 0

        # for letter in s:
        #     if letter == 'R':
        #         if stack['L'] != 0:
        #             stack['L'] -= 1
        #         else:
        #             stack['R'] += 1
        #     else:
        #         if stack['R'] != 0:
        #             stack['R'] -= 1
        #         else:
        #             stack['L'] += 1
        #     if stack['L'] == 0 and stack['R'] == 0:
        #         res += 1

        # return res

        stack = []
        res = 0
        
        for letter in s:
            if not stack:
                stack.append(letter)
            elif stack[-1] != letter:
                stack.pop()
                if not stack:
                    res += 1
            elif stack[-1] == letter:
                stack.append(letter)
        
        return res

def main():
    sol = Solution()
    print(sol.balancedStringSplit("RLRRLLRLRL"))
    print(sol.balancedStringSplit("RLLLLRRRLR"))
    print(sol.balancedStringSplit("LLLLRRRR"))

if __name__ == '__main__':
    main()