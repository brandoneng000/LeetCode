from typing import List
import collections

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped_q = collections.deque(popped)
        stack = []

        for val in pushed:
            stack.append(val)
            while popped_q and stack and popped_q[0] == stack[-1]:
                popped_q.popleft()
                stack.pop()
        
        return len(stack) == 0



def main():
    sol = Solution()
    print(sol.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]))
    print(sol.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))

if __name__ == '__main__':
    main()