class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_one = 0
        index_two = len(numbers) - 1

        while(True):
            if numbers[index_one] + numbers[index_two] > target:
                index_two -= 1
            elif numbers[index_one] + numbers[index_two] < target:
                index_one += 1
            else:
                return [index_one + 1, index_two + 1]

        # index_one = 0
        # index_two = 1
        # size_two = len(numbers)

        # while(index_one < len(numbers)):
        #     while(index_two < size_two):
        #         if numbers[index_one] + numbers[index_two] == target:
        #             return [index_one + 1, index_two + 1]
        #         if numbers[index_one] + numbers[index_two] > target:
        #             size_two = index_two
        #         index_two += 1
        #     index_one += 1
        #     index_two = index_one + 1

def main():
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    print(sol.twoSum([2, 7, 11, 15], 17))
    print(sol.twoSum([-1, 0], -1))
    print(sol.twoSum([5,25,75], 100))
    print(sol.twoSum([25,25,75], 50))

if __name__ == "__main__":
    main()