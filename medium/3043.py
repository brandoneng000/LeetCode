from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def count_prefix(arr: List[str]):
            res = set()

            for num in arr:
                for i in range(len(num) + 1):
                    res.add(num[:i])
        
            return res
        
        set_arr1 = count_prefix([str(num) for num in arr1])
        set_arr2 = count_prefix([str(num) for num in arr2])

        return len(max(set_arr1 & set_arr2, key=len))

        
def main():
    sol = Solution()
    print(sol.longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000]))
    print(sol.longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4]))

if __name__ == '__main__':
    main()