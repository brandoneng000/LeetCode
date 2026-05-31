from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        def helper(index: int, mass: int):
            if index == len(asteroids):
                return True

            if mass < asteroids[index]:
                return False
            
            if mass >= asteroids[-1]:
                return True
            
            return helper(index + 1, mass + asteroids[index])

        asteroids.sort()
        return helper(0, mass)

    # def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
    #     asteroids.sort()

    #     for a in asteroids:
    #         if mass < a:
    #             return False
    #         mass += a
        
    #     return True

        
def main():
    sol = Solution()
    print(sol.asteroidsDestroyed(mass = 10, asteroids = [3,9,19,5,21]))
    print(sol.asteroidsDestroyed(mass = 5, asteroids = [4,9,23,4]))

if __name__ == '__main__':
    main()