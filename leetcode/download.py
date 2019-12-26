import requests
import os
import time
import sys

URL = 'https://leetcode.com/api/submissions/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://leetcode.com/submissions/',
    'Cookie': ''
}
EXTENSIONS_MAP = {
    'python3': { 'ext': 'py', 'comment': '#' }, 
    'python2': { 'ext': 'py', 'comment': '#' }, 
    'python': { 'ext': 'py', 'comment': '#' }, 
    'c': { 'ext': 'c', 'comment': '//' }, 
    'c++': { 'ext': 'cpp', 'comment': '//' }, 
    'java': { 'ext': 'java', 'comment': '//' }, 
    'C#': { 'ext': 'cs', 'comment': '//' }, 
    'javascript': { 'ext': 'js', 'comment': '//' }, 
    'ruby': { 'ext': 'rb', 'comment': '#' }, 
    'swift': { 'ext': 'switch', 'comment': '//' }, 
    'go': { 'ext': 'go', 'comment': '//' },
    'scala': { 'ext': 'scala', 'comment': '//' },
    'kotlin': { 'ext': 'kt', 'comment': '//' },
    'rust': { 'ext': 'rs', 'comment': '//' },
    'php': { 'ext': 'php', 'comment': '//' },
    'mysql': { 'ext': 'sql', 'comment': '#' },
}
LOCAL_PATH = './'

def download():
    with open('./cookie') as fp:
        cookie = fp.read()
        HEADERS['Cookie'] = cookie
    session = requests.Session()
    session.headers.update(HEADERS)
    total = -1
    if len(sys.argv) == 2:
        total = int(sys.argv[1])
    offset = 0
    limit = 20
    while total < 0 or offset < total:
        resp = session.get(URL, params={'offset': offset, 'limit': limit})
        print('send request [{}]'.format(resp.url))
        if not resp.ok:
            print('request [{}] failed, status code: {}'.format(resp.url, resp.status_code))
            break
        print('request [{}] successed'.format(resp.url))
        data = resp.json()
        submissions = data.get('submissions_dump')
        if not isinstance(submissions, list):
            print('request [{}] received wrong data, response headers: {}, response data: {}'.format(resp.url, resp.headers, resp.text))
            break
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
            if os.path.exists(filepath):
                print('\tsubmission [{} - {}] was alread existed'.format(submission['title'], submission['id']))
                continue
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