codes = {"ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"}
rev = {v: k for k, v in codes.items()}
def decode(s:str) -> int:
    digits = []
    for i in range(0, len(s), 3):
        part = s[i:i+3]
        digits.append(codes[part])
    return int("".join(digits))
def encode(num: int) -> str:
    if num == 0:
        return "ZER"
    out = []
    for ch in str(num):
        out.append(rev[ch])
    return "".join(out)
expr = input().strip()
op_pos = -1
op = ""
for i, ch in enumerate(expr):
    if ch in "+-*":
        op_pos = i
        op = ch
        break
left = expr[:op_pos]
right = expr[op_pos+1:]

a = decode(left)
b = decode(right)

if op == "+":
    res = a+b
elif op == "-":
    res = a-b
else:
    res = a*b
    
print(encode(res))
