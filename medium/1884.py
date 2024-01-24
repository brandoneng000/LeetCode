class Solution:
    def twoEggDrop(self, n: int) -> int:
        res = 1
        cur = (res * (res + 1)) // 2

        while cur < n:
            res += 1
            cur = (res * (res + 1)) // 2
        
        return res
        

def main():
    sol = Solution()
    print(sol.twoEggDrop(2))
    print(sol.twoEggDrop(100))

if __name__ == '__main__':
    main()