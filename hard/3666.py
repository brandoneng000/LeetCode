from collections import deque
from bisect import bisect_left, bisect_right

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zero = s.count('0')
        
        if zero == 0:
            return 0
        
        unvisited = [
            list(range(0, n + 1, 2)),
            list(range(1, n + 1, 2))
        ]

        index = bisect_left(unvisited[zero % 2], zero)
        unvisited[zero % 2].pop(index)

        q = deque([(zero, 0)])

        while q:
            z, steps = q.popleft()

            zero_min = abs(z - k)
            zero_max = n - abs(n - z - k)

            target_parity = (z + k) % 2
            current_list = unvisited[target_parity]

            index_left = bisect_left(current_list, zero_min)
            index_right = bisect_right(current_list, zero_max)

            for i in range(index_left, index_right):
                zero_next = current_list[i]

                if zero_next == 0:
                    return steps + 1
                q.append((zero_next, steps + 1))
            
            del current_list[index_left: index_right]
        
        return -1

        
def main():
    sol = Solution()
    print(sol.minOperations(s = "110", k = 1))
    print(sol.minOperations(s = "0101", k = 3))
    print(sol.minOperations(s = "101", k = 2))

if __name__ == '__main__':
    main()