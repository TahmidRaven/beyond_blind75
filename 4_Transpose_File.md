# Problem 194 LEETCODE

- [Transpose File  – LeetCode](https://leetcode.com/problems/transpose-file/)

# Intuition


# Code 
```bash
#!/bin/bash

# Use awk to transpose the contents of the file
awk '
{
    # For each line, store each word in an array
    for (i = 1; i <= NF; i++) {
        arr[i] = (arr[i] ? arr[i] FS $i : $i)
    }
}
# After processing all lines, print the transposed result
END {
    for (i = 1; i <= length(arr); i++) {
        print arr[i]
    }
}
' file.txt
```
# Solution 

```
Input:
name age
alice 21
ryan 30

Output: 
name alice ryan
age 21 30

```
# Explaination: 

- **`NF`**: Stands for "Number of Fields," it tells you how many words there are in the current line.
- **`FS`**: Stands for "Field Separator," it defines how AWK splits a line into words (fields), usually by spaces or tabs.

- Shebang (#!/bin/bash)
Tells the system to run the script using the Bash shell.

- AWK Command
awk is used to process the file line by line.

- Processing Each Line:

- NF: Represents the number of fields (words) in the current line.

```for (i = 1; i <= NF; i++):``` Loops through each word in the line.

```arr[i]:``` Stores words in an array, with each column of the file being stored at a specific index in arr.

- Transposing Data:

```arr[i] = (arr[i] ? arr[i] FS $i : $i):``` Appends each word to the corresponding column in the array, ensuring spaces are preserved between words.

- END Block:

After all lines are processed, the END block prints each transposed column stored in arr.