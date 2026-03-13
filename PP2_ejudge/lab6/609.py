n = int(input())
keys = input().split()
values = input().split()
q = input()

d = dict(zip(keys, values))
print(d.get(q, "Not found"))