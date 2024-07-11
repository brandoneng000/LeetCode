from typing import List
from math import gcd

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        common_divisor = gcd(n, k)
        res = 0

        for i in range(common_divisor):
            temp = sorted([arr[j] for j in range(i, n, common_divisor)])
            median = temp[len(temp) // 2]
            res += sum(abs(num - median) for num in temp)
        
        return res
        
def main():
    sol = Solution()
    print(sol.makeSubKSumEqual(arr = [1,4,1,3], k = 2))
    print(sol.makeSubKSumEqual(arr = [2,5,5,7], k = 3))

if __name__ == '__main__':
    main()