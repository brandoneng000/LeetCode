from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)

        return stack
    # def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    #     stack = []

    #     for asteroid in asteroids:
    #         both = False
    #         if not stack:
    #             stack.append(asteroid)
    #         else:
    #             while stack and stack[-1] > 0 and asteroid < 0:
    #                 if stack[-1] > abs(asteroid):
    #                     break
    #                 elif stack[-1] == abs(asteroid):
    #                     stack.pop()
    #                     both = True
    #                     break
    #                 else:
    #                     stack.pop()
    #             if not both and (not stack or stack[-1] > 0 and asteroid > 0 or stack[-1] < 0 and asteroid < 0 or stack[-1] < 0 and asteroid > 0):
    #                 stack.append(asteroid)
                
    #     return stack

def main():
    sol = Solution()
    print(sol.asteroidCollision([5,10,-5]))
    print(sol.asteroidCollision([8,-8]))
    print(sol.asteroidCollision([10,2,-5]))

if __name__ == '__main__':
    main()