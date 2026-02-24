def cyc(x, lis):
    for i in range(k):
        for x in lis:
            yield x
lis = list(map(str, input().split()))
k = int(input())
print(" ".join(map(str, cyc(k, lis))))