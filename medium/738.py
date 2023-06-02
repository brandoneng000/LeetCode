class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        nums = [int(num) for num in str(n)[::-1]]
        left = -1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] or (left != -1 and nums[left] == nums[i]):
                left = i
        
        if left == -1:
            return n
        for i in range(left):
            nums[i] = 9
        nums[left] -= 1

        return int("".join(str(num) for num in nums[::-1]))
        
    
def main():
    sol = Solution()
    print(sol.monotoneIncreasingDigits(120))
    print(sol.monotoneIncreasingDigits(668841))
    print(sol.monotoneIncreasingDigits(1033))
    print(sol.monotoneIncreasingDigits(10))
    print(sol.monotoneIncreasingDigits(1234))
    print(sol.monotoneIncreasingDigits(332))

if __name__ == '__main__':
    main()