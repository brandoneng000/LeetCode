class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s

        # for index, letter in enumerate(s):
        #     if letter == goal[0]:
        #         temp = s[index:] + s[:index]
        #         if temp == goal:
        #             return True
            
        # return False

        
def main():
    sol = Solution()
    print(sol.rotateString("abcde", "cdeab"))
    print(sol.rotateString("abcde", "abced"))

if __name__ == '__main__':
    main()