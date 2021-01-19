z = 0
n = int(input())
ar = list(map(int, input().rstrip().split()))[:n]
for x in ar:
    z = z + x
print(z)