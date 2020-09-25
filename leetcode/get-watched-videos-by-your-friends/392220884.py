# title: get-watched-videos-by-your-friends
# detail: https://leetcode.com/submissions/detail/392220884/
# datetime: Mon Sep  7 16:35:12 2020
# runtime: 308 ms
# memory: 15.5 MB

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = collections.deque([id])
        cnt = collections.Counter()
        seen = {id}
        l = 0
        while q and l <= level:
            for i in range(len(q)):
                f = q.popleft()
                if l == level:
                    cnt.update(watchedVideos[f])
                for j in friends[f]:
                    if j not in seen:
                        q.append(j)
                        seen.add(j)
            l += 1
        return sorted(cnt.keys(), key=lambda k: (cnt[k], k))