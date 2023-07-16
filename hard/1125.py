from typing import List

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m = len(req_skills), len(people)
        skill_id = {}
        dp = { 0:[] }

        for i, skill in enumerate(req_skills):
            skill_id[skill] = i

        for i, p in enumerate(people):
            cur_skill = 0
            for skill in p:
                if skill in skill_id:
                    cur_skill |= 1 << skill_id[skill]
            
            for prev, need in dict(dp).items():
                combine = prev | cur_skill
                if combine == prev:
                    continue
                if combine not in dp or len(dp[combine]) > len(need) + 1:
                    dp[combine] = need + [i]
        
        return dp[(1 << n) - 1]


    # def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
    #     n = len(people)
    #     self.res = None

    #     def helper(required: set, hired: set):
    #         if not required:
    #             if not self.res or len(hired) < len(self.res):
    #                 self.res = hired.copy()
    #             return
            
    #         for i in range(n):
    #             if i not in hired:
    #                 hired.add(i)
    #                 helper(required - set(people[i]), hired)
    #                 hired.remove(i)
        
    #     helper(set(req_skills), set())
    #     return list(self.res)

def main():
    sol = Solution()
    print(sol.smallestSufficientTeam(req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]))
    print(sol.smallestSufficientTeam(req_skills = ["algorithms","math","java","reactjs","csharp","aws"], 
                                     people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]))

if __name__ == '__main__':
    main()