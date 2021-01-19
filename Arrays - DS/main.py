def reverseArray(a):
    a.reverse()
    return a


if __name__ == '__main__':
    arr_count = int(input())
    arr = list(map(int, input().strip().split()))[:arr_count]
    res = reverseArray(arr)
    for i in res:
        print(i, end=" ")
