from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 1000000007
        res = 0
        odds = 0
        evens = 0

        for val in arr:
            evens += 1

            if val % 2:
                odds, evens = evens, odds
            
            res += odds
            
        return res % mod

        
def main():
    sol = Solution()
    print(sol.numOfSubarrays([1,3,5]))
    print(sol.numOfSubarrays([2,4,6]))
    print(sol.numOfSubarrays([1,2,3,4,5,6,7]))

if __name__ == '__main__':
    main()