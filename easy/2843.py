class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0

        for num in range(low, high + 1):
            num_str = str(num)

            if len(num_str) % 2 == 1:
                continue
            first = sum(int(num_str[i]) for i in range(len(num_str) // 2))
            second = sum(int(num_str[i]) for i in range(len(num_str) // 2, len(num_str)))
            res += first == second
        
        return res
        
def main():
    sol = Solution()
    print(sol.countSymmetricIntegers(low = 1, high = 100))
    print(sol.countSymmetricIntegers(low = 1200, high = 1230))

if __name__ == '__main__':
    main()