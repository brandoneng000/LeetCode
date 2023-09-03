from typing import List

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = { v: [0] * len(votes[0]) + [v] for v in votes[0] }

        for vote in votes:
            for i, v in enumerate(vote):
                count[v][i] -= 1

        return ''.join(sorted(votes[0], key=count.get))
        
def main():
    sol = Solution()
    print(sol.rankTeams(["FVSHJIEMNGYPTQOURLWCZKAX","AITFQORCEHPVJMXGKSLNZWUY","OTERVXFZUMHNIYSCQAWGPKJL",
                         "VMSERIJYLZNWCPQTOKFUHAXG","VNHOZWKQCEFYPSGLAMXJIUTR","ANPHQIJMXCWOSKTYGULFVERZ",
                         "RFYUXJEWCKQOMGATHZVILNSP","SCPYUMQJTVEXKRNLIOWGHAFZ","VIKTSJCEYQGLOMPZWAHFXURN",
                         "SVJICLXKHQZTFWNPYRGMEUAO","JRCTHYKIGSXPOZLUQAVNEWFM","NGMSWJITREHFZVQCUKXYAPOL",
                         "WUXJOQKGNSYLHEZAFIPMRCVT","PKYQIOLXFCRGHZNAMJVUTWES","FERSGNMJVZXWAYLIKCPUQHTO",
                         "HPLRIUQMTSGYJVAXWNOCZEKF","JUVWPTEGCOFYSKXNRMHQALIZ","MWPIAZCNSLEYRTHFKQXUOVGJ",
                         "EZXLUNFVCMORSIWKTYHJAQPG","HRQNLTKJFIEGMCSXAZPYOVUW","LOHXVYGWRIJMCPSQENUAKTZF",
                         "XKUTWPRGHOAQFLVYMJSNEIZC","WTCRQMVKPHOSLGAXZUEFYNJI"]))
    print(sol.rankTeams(["BCA","CAB","CBA","ABC","ACB","BAC"]))
    print(sol.rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
    print(sol.rankTeams(["WXYZ","XYZW"]))
    print(sol.rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))

if __name__ == '__main__':
    main()