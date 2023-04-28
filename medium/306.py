class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        self.ans = []

        def helper(index, nums):
            if index == len(nums) and len(self.ans) >= 3:
                return True
            
            for i in range(index, len(nums)):
                if nums[index] == '0' and i != index:
                    break
                n = int(nums[index: i + 1])

                if len(self.ans) >= 2 and self.ans[-2] + self.ans[-1] < n:
                    break

                if len(self.ans) <= 1 or self.ans[-2] + self.ans[-1] == n:
                    self.ans.append(n)
                    if helper(i + 1, nums):
                        return True
                    self.ans.pop()

            return False
        
        helper(0, num)
        return len(self.ans) > 0
        


def main():
    sol = Solution()
    print(sol.isAdditiveNumber("112358"))
    print(sol.isAdditiveNumber("199100199"))
    print(sol.isAdditiveNumber("00112"))
    print(sol.isAdditiveNumber("0112"))

if __name__ == '__main__':
    main()