from typing import List
import collections

class TweetCounts:

    def __init__(self):
        self.tweet_names = collections.defaultdict(collections.Counter)
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweet_names[tweetName][time] += 1
        
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        chunks = { "minute": 60, "hour": 3600, "day": 86400 }
        res = [0 for _ in range(startTime, endTime + 1, chunks[freq])]

        for time in self.tweet_names[tweetName]:
            if startTime <= time <= endTime:
                res[(time - startTime + 1) // chunks[freq]] += self.tweet_names[tweetName][time]
        
        return res


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)