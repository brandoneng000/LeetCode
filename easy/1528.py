from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res_dict = {}
        res = ""

        for index, num in enumerate(indices):
            res_dict[num] = s[index]

        for key in range(len(indices)):
            res += res_dict[key]

        return res
        

        

def main():
    sol = Solution()
    print(sol.restoreString("codeleet", [4,5,6,7,0,2,1,3]))
    print(sol.restoreString("abc", [0,1,2]))

if __name__ == '__main__':
    main()