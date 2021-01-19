z = 0
n = int(input())
ar = list(map(int, input().split()))[:n]
for f in ar:
    z = z + f
print(z)
