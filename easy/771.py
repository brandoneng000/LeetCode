class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_dict = {}

        for jewel in jewels:
            jewel_dict[jewel] = 0

        for stone in stones:
            if stone in jewel_dict:
                jewel_dict[stone] += 1

        return sum(jewel_dict.values())
        
def main():
    sol = Solution()
    print(sol.numJewelsInStones("aA", "aAAbbbb"))

if __name__ == '__main__':
    main()