# title: subdomain-visit-count
# detail: https://leetcode.com/submissions/detail/411034298/
# datetime: Tue Oct 20 19:49:09 2020
# runtime: 48 ms
# memory: 14.2 MB

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = collections.Counter()
        for cp in cpdomains:
            cnt, domain = cp.split(' ')
            cnt = int(cnt)
            i = domain.find('.')
            j = domain.rfind('.')
            counter[domain] += cnt
            counter[domain[i + 1:]] += cnt
            if i != j:
                counter[domain[j + 1:]] += cnt
        return ['{} {}'.format(domain, cnt) for cnt, domain in counter.items()]
            