class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        left, right = 0, 100000

        while left < right:
            length = (left + right) // 2
            if length * length * length * 4 + length * length * 6 + length * 2 >= neededApples:
                right = length
            else:
                left = length + 1
            
        return left * 8

    # def minimumPerimeter(self, neededApples: int) -> int:
    #     length = 0
    #     apples = 0

    #     while apples < neededApples:
    #         length += 1
    #         apples += length * 8
    #         apples += length * 8 * length
    #         for i in range(1, length):
    #             apples += i * 8
        
    #     return length * 8


def main():
    sol = Solution()
    print(sol.minimumPerimeter(1))
    print(sol.minimumPerimeter(13))
    print(sol.minimumPerimeter(1000000000))

if __name__ == '__main__':
    main()