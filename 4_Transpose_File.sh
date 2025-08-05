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
