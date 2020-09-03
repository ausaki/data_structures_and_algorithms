# title: design-browser-history
# detail: https://leetcode.com/submissions/detail/381120899/
# datetime: Sat Aug 15 15:25:21 2020
# runtime: 240 ms
# memory: 16.1 MB

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.last = 0
        
    def visit(self, url: str) -> None:
        self.last
        self.curr += 1
        if self.curr < len(self.history):
            self.history[self.curr] = url
        else:
            self.history.append(url)
        self.last = self.curr

    def back(self, steps: int) -> str:
        self.curr -= min(steps, self.curr)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr += min(steps, self.last - self.curr)
        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)