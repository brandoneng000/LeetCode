from typing import List
import collections

class Twitter:
    def __init__(self):
        self.tweet_time = []
        # { tweet_id: user_id }
        self.tweet_user = {}
        # creates users
        self.users = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_time.append(tweetId)
        self.tweet_user[tweetId] = userId

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = []
        for i in range(len(self.tweet_time) - 1, -1, -1):
            tweet_id = self.tweet_time[i]
            if self.tweet_user[tweet_id] in self.users[userId] or self.tweet_user[tweet_id] == userId:
                news_feed.append(tweet_id)
                if len(news_feed) == 10:
                    break
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)