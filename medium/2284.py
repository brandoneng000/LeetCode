from typing import List
from collections import Counter

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        users = Counter()
        res = []

        for m, s in zip(messages, senders):
            users[s] += m.count(' ') + 1

        for u, count in users.most_common():
            if not res:
                res.append(u)
            if users[res[-1]] == count:
                res.append(u)
            else:
                break

        return max(res)
    
def main():
    sol = Solution()
    print(sol.largestWordCount(messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]))
    print(sol.largestWordCount(messages = ["How is leetcode for everyone","Leetcode is useful for practice"], senders = ["Bob","Charlie"]))

if __name__ == '__main__':
    main()