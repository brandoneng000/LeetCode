from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pieces_dict = {}
        result = []

        for piece in pieces:
            pieces_dict[piece[0]] = piece

        for num in arr:
            if num in pieces_dict:
                result += pieces_dict[num]
        
        return arr == result

def main():
    sol = Solution()
    print(sol.canFormArray(arr = [15,88], pieces = [[88],[15]]))
    print(sol.canFormArray(arr = [49,18,16], pieces = [[16,18,49]]))
    print(sol.canFormArray(arr = [91,4,64,78], pieces = [[78],[4,64],[91]]))

if __name__ == '__main__':
    main()