from typing import List
import collections

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0

        q = collections.deque([(0, "0000")])
        visited = set(deadends)
        visited.add("0000")

        while q:
            dist, combo = q.popleft()
            temp = []
            
            for index, digit in enumerate(combo):
                up = combo[:index] + str((int(digit) + 1) % 10) + combo[index + 1:]
                down = combo[:index] + str((int(digit) - 1) % 10) + combo[index + 1:]
                temp.append(up)
                temp.append(down)
            
            for c in temp:
                if c in visited:
                    continue
                visited.add(c)
                if c == target:
                    return dist + 1
                q.append((dist + 1, c))

        return -1

def main():
    sol = Solution()
    print(sol.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))
    print(sol.openLock(deadends = ["8888"], target = "0009"))
    print(sol.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))

if __name__ == '__main__':
    main()