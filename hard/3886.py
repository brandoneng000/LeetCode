from typing import List

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        def kmp(nums1, nums2):
            n, m = len(nums1), len(nums2)

            pi = [0] * m
            j = 0

            for i in range(1, m):
                while j > 0 and nums2[i] != nums2[j]:
                    j = pi[j - 1]

                if nums2[i] == nums2[j]:
                    j += 1

                pi[i] = j

            j = 0

            for i in range(n):
                while j > 0 and nums1[i] != nums2[j]:
                    j = pi[j - 1]

                if nums1[i] == nums2[j]:
                    j += 1

                if j == m:
                    return True

            return False

        def check(nums1, nums2):
            return kmp(nums1 + nums1, nums2)
        
        n = len(nums)

        fac = []

        for x in range(1, int(n ** 0.5) + 1):
            if n % x == 0:
                fac.append(x)

                if n // x != x:
                    fac.append(n // x)

        target = sorted(nums)
        res = 0

        for d in fac:
            for left in range(0, n, d):
                right = left + d - 1

                if not check(nums[left: right + 1], target[left: right + 1]):
                    break
            else:
                res += d

        return res


def main():
    sol = Solution()
    print(sol.sortableIntegers([3,1,2]))
    print(sol.sortableIntegers([7,6,5]))
    print(sol.sortableIntegers([5,8]))

if __name__ == '__main__':
    main()