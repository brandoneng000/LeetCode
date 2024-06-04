class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for i in range(num + 1):
            if i + int(str(i)[::-1]) == num:
                return True
        
        return False
        
def main():
    sol = Solution()
    print(sol.sumOfNumberAndReverse(443))
    print(sol.sumOfNumberAndReverse(63))
    print(sol.sumOfNumberAndReverse(181))

if __name__ == '__main__':
    main()