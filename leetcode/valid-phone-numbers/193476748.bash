# title: valid-phone-numbers
# detail: https://leetcode.com/submissions/detail/193476748/
# datetime: Wed Dec  5 15:22:35 2018
# runtime: 12 ms
# memory: N/A

# Read from the file file.txt and output all valid phone numbers to stdout.
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
