# title: unique-email-addresses
# detail: https://leetcode.com/submissions/detail/403912567/
# datetime: Sat Oct  3 21:44:06 2020
# runtime: 76 ms
# memory: 14.3 MB

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for em in emails:
            user, host = em.split('@')
            i = user.find('+')
            if i >= 0:
                user = user[:i]
            user = user.replace('.', '')
            s.add((user, host))
        return len(s)