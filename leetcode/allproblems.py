import requests

url = 'https://leetcode.com/api/problems/all/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://leetcode.com/submissions/',
    'Cookie': ''
}
with open('./cookie') as fp:
    cookie = fp.read()
    HEADERS['Cookie'] = cookie
resp = requests.get(url, headers=HEADERS)
data = resp.json()
num_total = data['num_total']
num_solved = data['num_solved']
ac_easy = data['ac_easy']
ac_medium = data['ac_medium']
ac_hard = data['ac_hard']
for k in ['num_total', 'num_solved', 'ac_easy', 'ac_medium', 'ac_hard']:
    print(f'{k}: {data[k]}')
problems = data['stat_status_pairs']
num_paid_only = 0
for problem in problems:
    if problem['paid_only']:
        num_paid_only += 1
print(f'{num_paid_only = }')