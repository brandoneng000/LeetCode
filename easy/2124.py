class Solution:
    def checkString(self, s: str) -> bool:
        return not ('ba' in s)
        
        # b = False
        # for letter in s:
        #     if letter == 'b':
        #         b = True
        #     if b and letter == 'a':
        #         return False
        
        # return True

def main():
    sol = Solution()
    print(sol.checkString("aaabbb"))
    print(sol.checkString("abab"))
    print(sol.checkString("bbb"))

if __name__ == '__main__':
    main()