from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        index_dict = { num: i for i, num in enumerate(sorted(set(arr)), 1) }

        return [index_dict[num] for num in arr]

    # def arrayRankTransform(self, arr: List[int]) -> List[int]:
    #     arr_ordered = sorted(list(set(arr)))
    #     arr_dict = {}

    #     for index, val in enumerate(arr_ordered, 1):
    #         arr_dict[val] = index
        
    #     for index, val in enumerate(arr):
    #         arr[index] = arr_dict[val]
        
    #     return arr

def main():
    sol = Solution()
    print(sol.arrayRankTransform([40,10,20,30]))
    print(sol.arrayRankTransform([100,100,100]))
    print(sol.arrayRankTransform([37,12,28,9,100,56,80,5,12]))

if __name__ == '__main__':
    main()