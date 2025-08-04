# Problem 217 LEETCODE

- [Contains Duplicate – LeetCode](https://leetcode.com/problems/tenth-line/]

# Intuition

- head -n 10 file.txt | tail -n 1
- ``` head -n 10 file.txt | tail -n 1```
was my initial solution; however leetcode didn't take it

# Code 
```
sed -n '10p;d' filename.txt
```
# Solution 

- -n: Suppresses automatic printing of all lines.

- '10p': Prints only the 10th line.

- 'd': Deletes all lines by default (used here to avoid printing others).
