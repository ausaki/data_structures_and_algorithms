# title: tweet-counts-per-frequency
# detail: https://leetcode.com/submissions/detail/387400514/
# datetime: Fri Aug 28 11:35:47 2020
# runtime: 356 ms
# memory: 21.4 MB

class TweetCounts:

    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweets:
            self.tweets[tweetName] = []
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        interval = 60
        if freq == 'hour':
            interval *= 60
        elif freq == 'day':
            interval *= 60 * 24
        tweets = self.tweets.get(tweetName)
        if tweets is None:
            return []
        i = bisect.bisect_left(tweets, startTime)
        n = len(tweets)
        result = []
        while startTime <= endTime:
            end = startTime + interval - 1
            end = min(end, endTime)
            j = bisect.bisect(tweets, end, i, n)
            result.append(j - i)
            i = j
            startTime = end + 1
        return result


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)