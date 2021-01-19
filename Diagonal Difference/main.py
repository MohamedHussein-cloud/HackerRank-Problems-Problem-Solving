i = 0
x = 0
a = 0
b = 0
n = int(input())
arr = list(map(int, input().rstrip().split()))[:n][:n]
for i in range(n):
    a = a + arr[[i][i]]
i = n
while i >= 0:
    b = b + arr[[x][i]]
    i = i - 1
    x = x + 1
