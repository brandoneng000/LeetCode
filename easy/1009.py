class Solution:
    def bitwiseComplement(self, n: int) -> int:
        mask = 1

        while n > mask:
            mask = mask * 2 + 1
        
        return mask ^ n

def main():
    sol = Solution()
    print(sol.bitwiseComplement(5))
    print(sol.bitwiseComplement(7))
    print(sol.bitwiseComplement(10))
    print(sol.bitwiseComplement(0))

if __name__ == '__main__':
    main()