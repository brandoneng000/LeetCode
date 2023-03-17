class Solution:
    def countPoints(self, rings: str) -> int:
        colors_dict = { 'R': set(), 'G': set(), 'B': set() }
        result = 0

        for index in range(0, len(rings), 2):
            colors_dict[rings[index]].add(int(rings[index + 1]))

        for ring in colors_dict[min(colors_dict, key=lambda x: colors_dict[x])]:
            if ring in colors_dict['R'] and ring in colors_dict['G'] and ring in colors_dict['B']:
                result += 1
        
        return result



def main():
    sol = Solution()
    print(sol.countPoints("B0B6G0R6R0R6G9"))
    print(sol.countPoints("B0R0G0R9R0B0G0"))
    print(sol.countPoints("G4"))

if __name__ == '__main__':
    main()