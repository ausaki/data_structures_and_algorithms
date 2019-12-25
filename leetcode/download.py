import requests
import os
import time

URL = 'https://leetcode.com/api/submissions/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://leetcode.com/submissions/',
    'Cookie': '__cfduid=d81d0a3a5e1642c7f7c6ca5af899f477e1575542088; csrftoken=qgHRGwqQvxSDeXAYSqex4tLXPmTAaI035Bg8GaE47H3XTSSDEZziCTkWQP5u1whZ; _ga=GA1.2.881666009.1575542090; _gid=GA1.2.822719810.1575542090; __atuvc=6%7C49%2C58%7C50%2C33%7C51%2C6%7C52; c_a_u="TC14bQ==:1ijlRW:fnmXegBeRtPDm1CgRrQAcoQhwmU"; __stripe_mid=ee5a4da2-f83b-4bae-ad7f-de8e15100b0d; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjMxMDU0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzcxOTEzZjk2ZTFkNGI4ZTAwNjE5YTcyOWY0MjIyM2ZkYjQ4ZTlmNiIsImlkIjoyMzEwNTQsImVtYWlsIjoibHhtNDJAZm94bWFpbC5jb20iLCJ1c2VybmFtZSI6IkwteG0iLCJ1c2VyX3NsdWciOiJsLXhtIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2wteG0vYXZhdGFyXzE1MjI0MDQ2NzgucG5nIiwidGltZXN0YW1wIjoiMjAxOS0xMi0xOSAxMzo1MzowOC45MDk3NzMrMDA6MDAiLCJJUCI6IjQ3LjUyLjY0LjUxIiwiSURFTlRJVFkiOiJiNTJlZGU2MjJhZGY1ZWYxMzFkNjZmOTY3NDFhOThhNiIsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.GtDeol71XD-1PZg7PQUOkS6VRpgcUBMtxxlDF3y1M4M'
}
EXTENSIONS_MAP = {
    'python3': {
        'ext': 'py',
        'comment': '#'
    },
    'python2': {
        'ext': 'py',
        'comment': '#'
    },
    'python': {
        'ext': 'py',
        'comment': '#'
    },
    'c': {
        'ext': 'c',
        'comment': '//'
    },
    'c++': {
        'ext': 'cpp',
        'comment': '//'
    },
    'java': {
        'ext': 'java',
        'comment': '//'
    },
    'C#': {
        'ext': 'cs',
        'comment': '//'
    },
    'javascript': {
        'ext': 'js',
        'comment': '//'
    },
    'ruby': {
        'ext': 'rb',
        'comment': '#'
    },
    'swift': {
        'ext': 'switch',
        'comment': '//'
    },
    'go': {
        'ext': 'go',
        'comment': '//'
    },
    'scala': {
        'ext': 'scala',
        'comment': '//'
    },
    'kotlin': {
        'ext': 'kt',
        'comment': '//'
    },
    'rust': {
        'ext': 'rs',
        'comment': '//'
    },
    'php': {
        'ext': 'php',
        'comment': '//'
    },
    'mysql': {
        'ext': 'sql',
        'comment': '#'
    },
}
LOCAL_PATH = './'

def download():
    session = requests.Session()
    session.headers.update(HEADERS)
    offset = 0
    limit = 20
    while True:
        resp = session.get(URL, params={'offset': offset, 'limit': limit})
        print('send request [{}]'.format(resp.url))
        if not resp.ok:
            print('request [{}] failed, status code: {}'.format(resp.url, resp.status_code))
            continue
        print('request [{}] successed'.format(resp.url))
        data = resp.json()
        submissions = data.get('submissions_dump')
        if not isinstance(submissions, list):
            print('request [{}] received wrong data, response headers: {}, response data: {}'.format(resp.url, resp.headers, resp.text))
        for submission in submissions:
            if submission['status_display'] != 'Accepted':
                print('\tsubmission [{} - {}] was not accepted'.format(submission['title'], submission['id']))
                continue
            title = submission['title']
            title = title.lower().replace(' ', '-')
            directory = os.path.join(LOCAL_PATH, title)
            if not os.path.exists(directory):
                os.mkdir(directory)
            lang = submission['lang']
            ext = lang
            comment = '#'
            if lang in EXTENSIONS_MAP:
                ext = EXTENSIONS_MAP[lang]['ext']
                comment = EXTENSIONS_MAP[lang]['comment']
            filename = '{}.{}'.format(submission['id'], ext)
            filepath = os.path.join(directory, filename)
            with open(filepath, 'w') as fp:
                fp.write('{} title: {}\n'.format(comment, title))
                fp.write('{} detail: https://leetcode.com{}\n'.format(comment, submission['url']))
                fp.write('{} datetime: {}\n'.format(comment, time.ctime(submission['timestamp'])))
                fp.write('{} runtime: {}\n'.format(comment, submission['runtime']))
                fp.write('{} memory: {}\n'.format(comment, submission['memory']))
                fp.write('\n')
                fp.write(submission['code'])
            print('\tsubmission [{} - {}] was downloaded'.format(submission['title'], submission['id']))
        l = len(submissions)
        if l < limit:
            break
        offset += l
        time.sleep(2)

if __name__ == '__main__':
    download()