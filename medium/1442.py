from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix = [0] + arr
        n = len(prefix)
        res = 0

        for i in range(n - 1):
            prefix[i + 1] ^= prefix[i]
        
        for i in range(n):
            for j in range(i + 1, n):
                if prefix[i] == prefix[j]:
                    res += j - i - 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.countTriplets([2,3,1,6,7]))
    print(sol.countTriplets([1,1,1,1,1]))

if __name__ == '__main__':
    main()