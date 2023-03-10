class Solution:
    def minimumMoves(self, s: str) -> int:
        # result = 0
        # s = list(s)
        # for index in range(len(s)):
        #     if s[index] == 'X':
        #         s[index] = 'O'
        #         if index < len(s) - 1 and s[index + 1] == 'X':
        #             s[index + 1] = 'O'
        #         if index < len(s) - 2 and s[index + 2] == 'X':
        #             s[index + 2] = 'O'
        #         result += 1
        
        # return result
        result = 0
        index = 0
        while index < len(s):
            if s[index] == 'X':
                result += 1
                index += 2
            index += 1
        
        return result

def main():
    sol = Solution()
    print(sol.minimumMoves("XXX"))
    print(sol.minimumMoves("XXOX"))
    print(sol.minimumMoves("OOOO"))
    print(sol.minimumMoves("OXOX"))

if __name__ == '__main__':
    main()