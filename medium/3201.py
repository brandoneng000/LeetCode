from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        parity = [num % 2 for num in nums]
        res = max(parity.count(1), parity.count(0))
        odd_even = 0
        odd_even_cur = 1
        even_odd = 0
        even_odd_cur = 0

        for i in range(n):
            if parity[i] == 0:
                if odd_even_cur == parity[i]:
                    odd_even += 1
                    odd_even_cur = 1
                
                if even_odd_cur == parity[i]:
                    even_odd += 1
                    even_odd_cur = 1
            else:
                if odd_even_cur == parity[i]:
                    odd_even += 1
                    odd_even_cur = 0
                
                if even_odd_cur == parity[i]:
                    even_odd += 1
                    even_odd_cur = 0

        return max(res, even_odd, odd_even)


        
        
def main():
    sol = Solution()
    print(sol.maximumLength([1,2,3,4]))
    print(sol.maximumLength([1,2,1,1,2,1,2]))
    print(sol.maximumLength([1,3]))

if __name__ == '__main__':
    main()