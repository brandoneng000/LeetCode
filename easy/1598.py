from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if ".." in log and stack:
                stack.pop()
            elif "." in log:
                pass
            else:
                stack.append(log)
        
        return len(stack)


def main():
    sol = Solution()
    print(sol.minOperations(["d1/","d2/","../","d21/","./"]))
    print(sol.minOperations(["d1/","d2/","./","d3/","../","d31/"]))
    print(sol.minOperations(["d1/","../","../","../"]))

if __name__ == '__main__':
    main()