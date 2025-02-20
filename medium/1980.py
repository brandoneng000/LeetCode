from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = 2 ** len(nums[0])
        nums_set = set(int(bits, 2) for bits in nums)

        for i in range(n):
            if i not in nums_set:
                return bin(i)[2:].zfill(len(nums[0]))


    # def findDifferentBinaryString(self, nums: List[str]) -> str:
    #     res = []

    #     for i in range(len(nums)):
    #         cur = nums[i][i]
    #         res.append('1' if cur == '0' else '0')
        
    #     return "".join(res)
    
    # def findDifferentBinaryString(self, nums: List[str]) -> str:
    #     def gen_binary(cur: List[str]):
    #         if len(cur) == bits:
    #             binaries.append("".join(cur))
    #             return

    #         for bit in ['0', '1']:
    #             cur.append(bit)
    #             gen_binary(cur)
    #             cur.remove(bit)
        
    #     bits = len(nums[0])
    #     binaries = []
    #     gen_binary([])

    #     return list(set(binaries) - set(nums))[0]
        
def main():
    sol = Solution()
    print(sol.findDifferentBinaryString(["01","10"]))
    print(sol.findDifferentBinaryString(["00","01"]))
    print(sol.findDifferentBinaryString(["111","011","001"]))

if __name__ == '__main__':
    main()