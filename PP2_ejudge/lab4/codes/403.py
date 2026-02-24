import sys

def div_by_3_and_4(n):
    for i in range(0, n + 1, 12):
        yield i

n = int(sys.stdin.readline())

out = sys.stdout.write
first = True
for x in div_by_3_and_4(n):
    if first:
        out(str(x))
        first = False
    else:
        out(" " + str(x))