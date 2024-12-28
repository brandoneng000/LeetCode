from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        best_start_first = 0
        best_start_second = [0, k]
        best_start_third = [0, k, k * 2]

        cur_window_first = sum(nums[:k])
        cur_window_second = sum(nums[k: k * 2])
        cur_window_third = sum(nums[k * 2: k * 3])

        best_single_sum = cur_window_first
        best_double_sum = cur_window_first + cur_window_second
        best_triple_sum = cur_window_first + cur_window_second + cur_window_third

        index_single = 1
        index_double = k + 1
        index_triple = k * 2 + 1

        while index_triple <= n - k:
            cur_window_first = cur_window_first - nums[index_single - 1] + nums[index_single + k - 1]
            cur_window_second = cur_window_second - nums[index_double - 1] + nums[index_double + k - 1]
            cur_window_third = cur_window_third - nums[index_triple - 1] + nums[index_triple + k - 1]

            if cur_window_first > best_single_sum:
                best_start_first = index_single
                best_single_sum = cur_window_first
            
            if cur_window_second + best_single_sum > best_double_sum:
                best_start_second[0] = best_start_first
                best_start_second[1] = index_double
                best_double_sum = cur_window_second + best_single_sum

            if cur_window_third + best_double_sum > best_triple_sum:
                best_start_third[0] = best_start_second[0]
                best_start_third[1] = best_start_second[1]
                best_start_third[2] = index_triple
                best_triple_sum = cur_window_third + best_double_sum

            index_single += 1
            index_double += 1
            index_triple += 1
        
        return best_start_third

        
def main():
    sol = Solution()
    print(sol.maxSumOfThreeSubarrays(nums = [1,2,1,2,6,7,5,1], k = 2))
    print(sol.maxSumOfThreeSubarrays(nums = [1,2,1,2,1,2,1,2,1], k = 2))

if __name__ == '__main__':
    main()