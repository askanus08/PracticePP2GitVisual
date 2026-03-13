n = int(input())
words = input().split()
print(*[str(i) + ':' + word for i, word in enumerate(words)])