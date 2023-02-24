from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # for num in range(1, area + 1):
        #     if area % num == 0 and num >= area // num:
        #         return [num, area // num]

        for num in range(int(area ** 0.5), 0, -1):
            if area % num == 0:
                return [area // num, num]

def main():
    sol = Solution()
    print(sol.constructRectangle(4))
    print(sol.constructRectangle(37))
    print(sol.constructRectangle(122122))

if __name__ == '__main__':
    main()