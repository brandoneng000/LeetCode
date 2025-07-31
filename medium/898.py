from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()

        for x in arr:
            cur = {x | y for y in cur} | {x}
            res |= cur
        
        return len(res)

    # def subarrayBitwiseORs(self, arr: List[int]) -> int:
    #     res = set(arr)
    #     prev = set()
    #     prev.add(arr[0])
    #     for n in arr[1:]:
    #         temp = set()
    #         for p in prev:
    #             temp.add(n | p)
    #             res.add(n | p)
    #         prev = temp
    #         prev.add(n)
        
    #     return len(res)
            
def main():
    sol = Solution()
    print(sol.subarrayBitwiseORs([0]))
    print(sol.subarrayBitwiseORs([1,1,2]))
    print(sol.subarrayBitwiseORs([1,2,4]))

if __name__ == '__main__':
    main()