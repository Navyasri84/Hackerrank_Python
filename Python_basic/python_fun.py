'''The included code stub will read an integer,n, from STDIN.
Without using any string methods, try to print the following:
123...n

Example:
n=5
Print the string 12345.

Input Format

The first line contains an integer n.'''

n = int(input())

for i in range(0, n+1):
    print(i,end='')