import sys

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(sys.stdin.readline())
it = even_numbers(n)

out = sys.stdout.write
first = True
for x in it:
    if first:
        out(str(x))
        first = False
    else:
        out("," + str(x))