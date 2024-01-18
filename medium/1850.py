from typing import List

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_permu(nums: List[str]):
            small = len(nums) - 2

            while small >= 0 and nums[small] >= nums[small + 1]:
                small -= 1
            
            if small == -1:
                nums.reverse()
            else:
                next_large = small + 1
                for i in range(n - 1, small, -1):
                    if nums[small] < nums[i]:
                        next_large = i
                        break
                
                nums[small], nums[next_large] = nums[next_large], nums[small]
                start = small + 1
                nums[start:] = nums[start:][::-1]
            return nums
            

        n = len(num)    
        original = list(num)
        num = list(num)
        res = 0

        for _ in range(k):
            num = next_permu(num)

        for i in range(n):
            j = num.index(original[i], i)
            res += j - i
            num[i: j + 1] = [num[j]] + num[i: j]
        
        return res

def main():
    sol = Solution()
    print(sol.getMinSwaps(num = "5489355142", k = 4))
    print(sol.getMinSwaps(num = "11112", k = 4))
    print(sol.getMinSwaps(num = "00123", k = 1))

if __name__ == '__main__':
    main()