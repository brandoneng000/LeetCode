from typing import List

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        INF = 10 ** 33
        smallest_odd = smallest_even = INF

        for num in nums1:
            if num % 2:
                smallest_odd = min(smallest_odd, num)
            else:
                smallest_even = min(smallest_even, num)

        if smallest_even == INF or smallest_odd == INF:
            return True

        if smallest_even < smallest_odd:
            return False

        return True

def main():
    sol = Solution()
    print(sol.uniformArray([1,4,7]))
    print(sol.uniformArray([2,3]))
    print(sol.uniformArray([4,6]))

if __name__ == '__main__':
    main()