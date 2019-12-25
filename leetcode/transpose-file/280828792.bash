# title: transpose-file
# detail: https://leetcode.com/submissions/detail/280828792/
# datetime: Fri Nov 22 17:03:15 2019
# runtime: 8 ms
# memory: 3.6 MB

# Read from the file file.txt and print its transposed content to stdout.
awk '
{ for(i = 1; i <= NF; i = i + 1){ lines[i] = lines[i] " " $i} } 
END { for(i = 1; i <= NF; i = i + 1){ print lines[i] } }' file.txt | sed -e 's/^ //'
