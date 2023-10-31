from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i - 1] ^ pref[i] for i in range(1, len(pref))]
    
    # def findArray(self, pref: List[int]) -> List[int]:
    #     n = len(pref)
    #     res = [pref[0]]

    #     for i in range(1, n):
    #         res.append(pref[i - 1] ^ pref[i])

    #     return res

        
def main():
    sol = Solution()
    print(sol.findArray([5,2,0,3,1]))
    print(sol.findArray([13]))

if __name__ == '__main__':
    main()