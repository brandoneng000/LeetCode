from typing import List

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [float('inf')]

        for val in arr:
            while stack[-1] <= val:
                mid = stack.pop()
                res += mid * min(stack[-1], val)
            stack.append(val)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        
        return res

    # def mctFromLeafValues(self, arr: List[int]) -> int:
    #     if len(arr) == 2:
    #         return arr[0] * arr[1]
    #     smallest_prod = float('inf')
    #     smallest_index = -1

    #     for i in range(len(arr) - 1):
    #         prod = arr[i] * arr[i + 1]
    #         if prod < smallest_prod:
    #             smallest_prod = prod
    #             smallest_index = i
        
    #     val = min(smallest_index, smallest_index + 1, key=lambda x: arr[x])
    #     arr.pop(val)
    #     return smallest_prod + self.mctFromLeafValues(arr)

def main():
    sol = Solution()
    print(sol.mctFromLeafValues([1,2,3,4,5]))
    print(sol.mctFromLeafValues([6,2,4]))
    print(sol.mctFromLeafValues([4,11]))

if __name__ == '__main__':
    main()