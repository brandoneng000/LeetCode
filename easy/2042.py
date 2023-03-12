class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        nums = []
        for word in s:
            if word.isnumeric():
                nums.append(int(word))
        
        for index in range(len(nums) - 1):
            if nums[index] >= nums[index + 1]:
                return False
            
        return True

def main():
    sol = Solution()
    print(sol.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
    print(sol.areNumbersAscending("hello world 5 x 5"))
    print(sol.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))

if __name__ == '__main__':
    main()