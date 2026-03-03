import re

s = input()
pat = re.compile(r"^\d+$")

print("Match" if pat.match(s) else "No match")