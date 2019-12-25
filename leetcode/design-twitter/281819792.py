# title: design-twitter
# detail: https://leetcode.com/submissions/detail/281819792/
# datetime: Tue Nov 26 21:21:57 2019
# runtime: 100 ms
# memory: 22 MB

from collections import deque, defaultdict
import heapq

class Twitter:
    FEEDS_SIZE = 10
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._time = 0
        self.user_tweets = defaultdict(list) # {user: }
        self.tweets = {} 
        self.feeds = defaultdict(lambda: deque(maxlen=self.FEEDS_SIZE)) # {user: feeds}
        self.followers = defaultdict(set) # {user: followers}
        self.followings = defaultdict(set) # {user: followings}
    
    def _now(self):
        self._time += 1
        return self._time
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[tweetId] = {'user': userId, 'create_time': self._now()}
        self.user_tweets[userId].append(tweetId)
        followers = self.followers[userId]
        for u in followers:
            self.feeds[u].appendleft(tweetId)
        self.feeds[userId].appendleft(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        return list(self.feeds[userId])
        
    def _genNewsFeed(self, userId):
        feeds = [(self.tweets[t]['create_time'], t) for t in self.user_tweets[userId][-10:]]
        heapq.heapify(feeds)
        followings = self.followings[userId]
        for u in followings:
            for t in self.user_tweets[u][-10:]:
                item = (self.tweets[t]['create_time'], t)
                if len(feeds) < 10:
                    heapq.heappush(feeds, item)
                else:
                    if item[0] > feeds[0][0]:
                        heapq.heappushpop(feeds, item)
        d = deque(maxlen=self.FEEDS_SIZE)
        while feeds:
            d.appendleft(heapq.heappop(feeds)[1])
        return d
    
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        if followeeId in self.followings[followerId]:
            return
        self.followers[followeeId].add(followerId)
        self.followings[followerId].add(followeeId)
        self.feeds[followerId] = self._genNewsFeed(followerId)
            
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        if followeeId not in self.followings[followerId]:
            return
        self.followers[followeeId].remove(followerId)
        self.followings[followerId].remove(followeeId)
        self.feeds[followerId] = self._genNewsFeed(followerId)
                



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)