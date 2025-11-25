from typing import List

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0

        for size in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k

            if remainder == 0:
                return size
        
        return -1

    # def smallestRepunitDivByK(self, k: int) -> int:
    #     r = 0
    #     size = 0
    #     remainders = set()
    #     while r not in remainders:
    #         remainders.add(r)
    #         r = ((r * 10) + 1) % k
    #         size += 1
    #         if r == 0:
    #             return size
            
    #     return -1

def main():
    sol = Solution()
    print(sol.smallestRepunitDivByK(1))
    print(sol.smallestRepunitDivByK(2))
    print(sol.smallestRepunitDivByK(3))

if __name__ == '__main__':
    main()