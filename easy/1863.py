from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # memory = {}
        # combination = []
        # result = 0
        
        # def recursive(index: int, stack: List[int], size: int):
        #     if len(stack) == size:
        #         combination.append(stack.copy())
            
        #     for i in range(index, len(nums)):
        #         stack.append(nums[i])
        #         recursive(i + 1, stack, size)
        #         stack.pop()

        # for s in range(1, len(nums) + 1):
        #     recursive(0, [], s)

        # for combo in combination:
        #     temp = tuple(combo)
        #     memory[temp] = memory.get(tuple(combo[:-1]), 0) ^ combo[-1]
        #     result += memory[temp]

        # return result

        memory = {}
        result = 0
        
        def recursive(index: int, stack: List[int], size: int) -> int:
            total = 0

            if len(stack) == size:
                temp = tuple(stack)
                memory[temp] = memory.get(tuple(stack[:-1]), 0) ^ stack[-1]
                return memory[temp]
            
            for i in range(index, len(nums)):
                stack.append(nums[i])
                total += recursive(i + 1, stack, size)
                stack.pop()
            
            return total

        for s in range(1, len(nums) + 1):
            result += recursive(0, [], s)

        return result
    
def main():
    sol = Solution()
    print(sol.subsetXORSum([1,3]))
    print(sol.subsetXORSum([5,1,6]))
    print(sol.subsetXORSum([3,4,5,6,7,8]))
    print(sol.subsetXORSum([1,1,1]))

if __name__ == '__main__':
    main()