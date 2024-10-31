from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        def helper(robot_index: int, factory_index: int):
            if dp[robot_index][factory_index] is not None:
                return dp[robot_index][factory_index]
            
            if robot_index == n:
                dp[robot_index][factory_index] = 0
                return 0
            
            if factory_index == m:
                dp[robot_index][factory_index] = 10 ** 12
                return 10 ** 12
            
            assign = abs(robot[robot_index] - factory_pos[factory_index]) + helper(robot_index + 1, factory_index + 1)
            
            skip = helper(robot_index, factory_index + 1)

            dp[robot_index][factory_index] = min(assign, skip)

            return dp[robot_index][factory_index]

        robot.sort()
        factory.sort(key=lambda x: x[0])
        factory_pos = []

        for f in factory:
            factory_pos.extend([f[0]] * f[1])
        
        n, m = len(robot), len(factory_pos)
        dp = [[None for j in range(m + 1)] for i in range(n + 1)]

        return helper(0, 0)

        
def main():
    sol = Solution()
    print(sol.minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]]))
    print(sol.minimumTotalDistance(robot = [1,-1], factory = [[-2,1],[2,1]]))

if __name__ == '__main__':
    main()