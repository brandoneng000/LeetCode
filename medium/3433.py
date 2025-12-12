from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), int(x[0] == "MESSAGE")))
        res = [0] * numberOfUsers
        everyone = 0
        offline = [-70] * numberOfUsers

        for message, time, users in events:
            time = int(time)

            if message == "MESSAGE":
                if users == "ALL":
                    everyone += 1
                    continue
                elif users == "HERE":
                    user_list = range(numberOfUsers)

                    for u in user_list:
                        if time >= offline[u]:
                            res[u] += 1

                else:
                    user_list = [int(u.lstrip("id")) for u in users.split()]
                
                    for u in user_list:
                        res[u] += 1
            else:
                offline[int(users)] = int(time) + 60
        
        return [u + everyone for u in res]

        
def main():
    sol = Solution()
    print(sol.countMentions(numberOfUsers = 3, events = [["MESSAGE","1","id0 id1"],["MESSAGE","5","id2"],["MESSAGE","6","ALL"],["OFFLINE","5","2"]]))
    print(sol.countMentions(numberOfUsers = 3, events = [["MESSAGE","2","HERE"],["OFFLINE","2","1"],["OFFLINE","1","0"],["MESSAGE","61","HERE"]]))
    print(sol.countMentions(numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]))
    print(sol.countMentions(numberOfUsers = 2, events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]))
    print(sol.countMentions(numberOfUsers = 2, events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]))

if __name__ == '__main__':
    main()