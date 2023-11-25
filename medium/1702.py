class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        if binary.count('0') <= 1:
            return binary
        
        n = len(binary)
        t = binary.find('0')
        k = binary.count('1', binary.find('0'))

        return '1' * (n - k - 1) + '0' + '1' * k

        
def main():
    sol = Solution()
    print(sol.maximumBinaryString("000110"))
    print(sol.maximumBinaryString("01"))

if __name__ == '__main__':
    main()