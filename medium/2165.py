class Solution:
    def smallestNumber(self, num: int) -> int:
        negative = False
        if num < 0:
            negative = True
            num *= -1
        elif num == 0:
            return num

        nums = list(str(num))
        zero = nums.count('0')
        nums.sort(reverse=negative)
        if not negative:
            nums[0], nums[zero] = nums[zero], nums[0]
        
        
        nums = int("".join(nums))
        return -nums if negative else nums


def main():
    sol = Solution()
    print(sol.smallestNumber(310))
    print(sol.smallestNumber(-7605))
    print(sol.smallestNumber(0))

if __name__ == '__main__':
    main()