alice = 0
bob = 0
z = {0, 1, 2}
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
for x in z:
    if a[x] < b[x]:
        alice = alice + 1
    elif a[x] > b[x]:
        bob = bob + 1
    else:
        continue
print(bob, alice)
