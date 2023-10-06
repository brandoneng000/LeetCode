from typing import List
import collections

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = collections.Counter()

        for n in arr:
            remainder_count[n % k] += 1
        
        if remainder_count[0] % 2:
            return False
        
        for i in range(1, k // 2 + 1):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        return True
        
def main():
    sol = Solution()
    print(sol.canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5))
    print(sol.canArrange(arr = [1,2,3,4,5,6], k = 7))
    print(sol.canArrange(arr = [1,2,3,4,5,6], k = 10))

if __name__ == '__main__':
    main()