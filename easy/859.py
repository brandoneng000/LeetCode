class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        differences_s = ""
        differences_goal = ""

        if len(s) != len(goal):
            return False

        if s == goal and len(set(s)) < len(s):
            return True

        for index, letter in enumerate(s):
            if letter != goal[index]:
                differences_s += letter
                differences_goal += goal[index]
        
        if len(differences_s) != 2:
            return False

        return "".join(sorted(differences_s)) == "".join(sorted(differences_goal))

        # if len(s) != len(goal):
        #     return False
        # swap = 0

        # while swap < len(s) - 1:
        #     index = swap + 1
        #     while index < len(s):
        #         if s[swap] != s[index]:
        #             letters = s[:swap] + s[index] + s[swap + 1:index] + s[swap] + s[index+1:]
        #             if goal == letters:
        #                 return True
        #         elif s == goal:
        #             return True
        #         index += 1
        #     swap += 1
        
        # return False
        

def main():
    sol = Solution()
    print(sol.buddyStrings("ab", "ba"))
    print(sol.buddyStrings("ab", "ab"))
    print(sol.buddyStrings("aa", "aa"))
    print(sol.buddyStrings("abc", "cba"))

if __name__ == '__main__':
    main()