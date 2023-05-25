import collections

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = collections.deque([])
        dire = collections.deque([])
        
        for i, t in enumerate(senate):
            if t == "R":
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if d < r:
                dire.append(d + len(senate))
            else:
                radiant.append(r + len(senate))
        
        return "Radiant" if radiant else "Dire"


def main():
    sol = Solution()
    print(sol.predictPartyVictory("DRRDRDRDRDDRDRDR"))
    print(sol.predictPartyVictory("RRRRRRRDDDDDDDDD"))
    print(sol.predictPartyVictory("RD"))
    print(sol.predictPartyVictory("RDD"))

if __name__ == '__main__':
    main()