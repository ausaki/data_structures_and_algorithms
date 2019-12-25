# title: transpose-file
# detail: https://leetcode.com/submissions/detail/280829114/
# datetime: Fri Nov 22 17:05:44 2019
# runtime: 4 ms
# memory: 3.5 MB

# Read from the file file.txt and print its transposed content to stdout.
awk '
{ for(i = 1; i <= NF; i = i + 1){ if(NR == 1) { lines[i] = $i } else {lines[i] = lines[i] " " $i}} } 
END { for(i = 1; i <= NF; i = i + 1){ print lines[i] } }' file.txt
