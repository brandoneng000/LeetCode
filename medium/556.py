class Solution:
    def nextGreaterElement(self, n: int) -> int:        
        num = list(str(n))
        i, j = len(num) - 1, len(num) - 2

        while i - 1 >= 0 and num[i] <= num[i - 1]:
            i -= 1
        
        if i == 0:
            return -1
        
        j = i
        while j < len(num) - 1 and num[j + 1] > num[i - 1]:
            j += 1
        
        num[i - 1], num[j] = num[j], num[i - 1]
        num[i:] = num[i:][::-1]
        res = int(''.join(num))

        return res if res < 1 << 31 else -1
        

def main():
    sol = Solution()
    print(sol.nextGreaterElement(12))
    print(sol.nextGreaterElement(21))
    print(sol.nextGreaterElement(2561251))

if __name__ == '__main__':
    main()