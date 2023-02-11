import collections

class Solution:
    # Find the number of lists with the same length
    def countLargestGroup(self, n: int) -> int:
        nums_dict = collections.defaultdict(list)
        
        for num in range(1, n+1):
            num = [int(digit) for digit in list(str(num))]
            nums_dict[sum(num)].append(num)
        
        largest_size = len(max(nums_dict.values(), key=len))
        result = 0
        for nums in nums_dict.values():
            result += len(nums) == largest_size

        return result

def main():
    sol = Solution()
    print(sol.countLargestGroup(13))
    print(sol.countLargestGroup(2))
    print(sol.countLargestGroup(19))

if __name__ == '__main__':
    main()