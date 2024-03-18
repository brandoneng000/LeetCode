from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        res = list(s)

        for i in spaces:
            res[i] = ' ' + res[i]
        
        return "".join(res)



        
def main():
    sol = Solution()
    print(sol.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))
    print(sol.addSpaces(s = "icodeinpython", spaces = [1,5,7,9]))
    print(sol.addSpaces(s = "spacing", spaces = [0,1,2,3,4,5,6]))

if __name__ == '__main__':
    main()