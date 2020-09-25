# title: defanging-an-ip-address
# detail: https://leetcode.com/submissions/detail/397106282/
# datetime: Fri Sep 18 01:16:53 2020
# runtime: 36 ms
# memory: 13.7 MB

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')