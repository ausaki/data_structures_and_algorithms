# title: design-authentication-manager
# detail: https://leetcode.com/submissions/detail/470205600/
# datetime: Sun Mar 21 00:21:36 2021
# runtime: 320 ms
# memory: 15.7 MB

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        t = self.tokens.get(tokenId, -1)
        if t <= currentTime:
            return
        self.generate(tokenId, currentTime)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(1 for t in self.tokens.values() if t > currentTime)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)