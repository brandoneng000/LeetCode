class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_dict = {}
        for index, val in enumerate(nums):
            if val in num_dict and index - num_dict[val] <= k:
                return True
            else:
                num_dict[val] = index
        return False


def main():
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,1], 3))
    print(sol.containsNearbyDuplicate([1,1,1,1,1,1,1,1,1], 3))
    print(sol.containsNearbyDuplicate([1,0,1,1], 1))
    print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))


if __name__ == '__main__':
    main()