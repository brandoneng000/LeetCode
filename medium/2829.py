class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        invalid = set([])
        count = 0
        res = 0

        for num in range(1, n + k + 1):
            if num in invalid: 
                continue
            
            res += num
            count += 1
            invalid.add(k - num)

            if count == n:
                break
        
        return res
        
def main():
    sol = Solution()
    print(sol.minimumSum(n = 5, k = 4))
    print(sol.minimumSum(n = 2, k = 6))

if __name__ == '__main__':
    main()