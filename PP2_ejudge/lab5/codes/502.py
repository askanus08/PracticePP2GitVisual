import re

S = input()
P = input()

print("Yes" if re.search(re.escape(P), S) else "No")