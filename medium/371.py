class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0b1111111111
        
        while(b & mask):
            a, b = (a ^ b), (a & b) << 1
        return a & mask if b > 0 else a

    

def main():
    sol = Solution()
    print(sol.getSum(1, 2))
    print(sol.getSum(2, 3))
    print(sol.getSum(2, -3))
    print(sol.getSum(-1, 1))

if __name__ == '__main__':
    main()