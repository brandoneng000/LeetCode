from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def helper(tasty: int):
            prev = price[0]
            count = 1

            for i in range(1, n):
                if price[i] - prev >= tasty:
                    count += 1
                    prev = price[i]
            
            return count >= k

        n = len(price)
        price.sort()
        left, right = 0, price[-1] - price[0] + 1

        while left < right:
            middle = (left + right) // 2

            if helper(middle):
                left = middle + 1
            else:
                right = middle
        
        return left - 1
        
        
def main():
    sol = Solution()
    print(sol.maximumTastiness(price = [13,5,1,8,21,2], k = 3))
    print(sol.maximumTastiness(price = [1,3,1], k = 2))

if __name__ == '__main__':
    main()