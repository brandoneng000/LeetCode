from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        left, right = 1, k + 1

        while left <= right:
            res.append(left)
            if left != right:
                res.append(right)
            left += 1
            right -= 1
        
        for i in range(len(res) + 1, n + 1):
            res.append(i)

        return res
        

def main():
    sol = Solution()
    print(sol.constructArray(n = 50, k = 30))
    print(sol.constructArray(n = 10, k = 2))
    print(sol.constructArray(n = 3, k = 1))
    print(sol.constructArray(n = 3, k = 2))

if __name__ == '__main__':
    main()