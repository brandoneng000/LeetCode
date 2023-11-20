
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 1000000007
        res = 0
        
        for num in range(1, n + 1):
            res = ((res << int.bit_length(num)) | num) % mod
        
        return res % mod

        
def main():
    sol = Solution()
    print(sol.concatenatedBinary(1))
    print(sol.concatenatedBinary(3))
    print(sol.concatenatedBinary(12))
    print(sol.concatenatedBinary(10000))

if __name__ == '__main__':
    main()