from typing import List

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        time = 1

        while True:
            if memory1 >= memory2:
                if time > memory1:
                    break
                else:
                    memory1 -= time
            else:
                if time > memory2:
                    break
                else:
                    memory2 -= time

            time += 1
        
        return [time, memory1, memory2]
        
def main():
    sol = Solution()
    print(sol.memLeak(memory1 = 2, memory2 = 2))
    print(sol.memLeak(memory1 = 8, memory2 = 11))

if __name__ == '__main__':
    main()