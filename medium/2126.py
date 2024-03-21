from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for a in asteroids:
            if mass < a:
                return False
            mass += a
        
        return True

        
def main():
    sol = Solution()
    print(sol.asteroidsDestroyed(mass = 10, asteroids = [3,9,19,5,21]))
    print(sol.asteroidsDestroyed(mass = 5, asteroids = [4,9,23,4]))

if __name__ == '__main__':
    main()