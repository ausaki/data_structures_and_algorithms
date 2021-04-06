# title: design-authentication-manager
# detail: https://leetcode.com/submissions/detail/470175722/
# datetime: Sat Mar 20 23:10:33 2021
# runtime: 192 ms
# memory: 15.9 MB

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}
        self.arr = []
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        # self.arr.append(currentTime + self.ttl)
        # self.tokens[tokenId] = len(self.arr) - 1
        self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        # i = self.tokens.get(tokenId, -1)
        # if i == -1:
        #     return 
        # t = self.arr[i]
        # if currentTime >= t:
        #     return 
        # self.arr.pop(i)
        # self.generate(tokenId, currentTime)
        # self.arr[i] = -1
        t = self.tokens.get(tokenId, -1)
        if t <= currentTime:
            return
        self.tokens[tokenId] = currentTime + self.ttl
            
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        i = bisect.bisect(sorted(self.tokens.values()), currentTime)
        return len(self.tokens) - i


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)