from typing import List
import bisect

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.lead = {}
        self.votes = {}
        leader, v = None, 0

        for i in range(len(times)):
            self.votes[persons[i]] = self.votes.get(persons[i], 0) + 1
            if self.votes[persons[i]] >= v:
                leader = persons[i]
                v = self.votes[persons[i]]
            
            self.lead[times[i]] = leader

    def q(self, t: int) -> int:
        index = bisect.bisect_left(self.times, t)
        if index >= len(self.times):
            index = len(self.times) - 1
        if self.times[index] > t:
            index -= 1
        
        return self.lead[self.times[index]]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)