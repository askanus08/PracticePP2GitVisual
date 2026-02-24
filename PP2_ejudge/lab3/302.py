def isUsual(num: int) -> bool:
    for i in (2, 3, 5):
        while num%i == 0:
            num //= i
    return num == 1
n = int(input().strip())
print("Yes" if isUsual(n) else "No")