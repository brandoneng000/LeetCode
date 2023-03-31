class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        res = 0

        for i in range(len(num_str) - (k - 1)):
            divisor = int(num_str[i: i + k])
            if divisor:
                res += (num % divisor == 0)
        
        return res
        

def main():
    sol = Solution()
    print(sol.divisorSubstrings(num = 240, k = 2))
    print(sol.divisorSubstrings(num = 430043, k = 2))

if __name__ == '__main__':
    main()