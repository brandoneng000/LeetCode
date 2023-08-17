from typing import List
import collections

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set([start])
        q = collections.deque([start])

        while q:
            index = q.popleft()

            if arr[index] == 0:
                return True

            forward = index + arr[index]
            backward = index - arr[index]
            
            if forward not in visited and 0 <= forward < n:
                visited.add(forward)
                q.append(forward)
            
            if backward not in visited and 0 <= backward < n:
                visited.add(backward)
                q.append(backward)

        return False
            


def main():
    sol = Solution()
    print(sol.canReach(arr = [4,2,3,0,3,1,2], start = 5))
    print(sol.canReach(arr = [4,2,3,0,3,1,2], start = 0))
    print(sol.canReach(arr = [3,0,2,1,2], start = 2))

if __name__ == '__main__':
    main()