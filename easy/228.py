class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        start = nums[0]
        counter = nums[0]
        for index in range(1, len(nums)):
            if nums[index] == counter + 1:
                counter += 1
            else:
                if start == counter:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{counter}")
                start = nums[index]
                counter = nums[index]
                
        if start == counter:
            res.append(str(start))
        else:
            res.append(f"{start}->{counter}")

        return res

        
def main():
    sol = Solution()
    print(sol.summaryRanges([0,1,2,4,5,7,9,10]))
    print(sol.summaryRanges([0,1,2,4,5,7]))
    print(sol.summaryRanges([2,3,6,7,8]))
    print(sol.summaryRanges([0,2,3,4,6,8,9]))
    print(sol.summaryRanges([]))
    print(sol.summaryRanges([-1]))

if __name__ == "__main__":
    main()