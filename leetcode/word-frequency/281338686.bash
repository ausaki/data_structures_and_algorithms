# title: word-frequency
# detail: https://leetcode.com/submissions/detail/281338686/
# datetime: Mon Nov 25 01:09:04 2019
# runtime: 0 ms
# memory: 3.3 MB

# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | sed 's/ \+/\n/g' | sed '/^$/d' | sort | uniq -c | sort -brn -k1 | awk '{print $2 " " $1}'