from datetime import date

def parse(line: str):
    d_str, tz_str = line.strip().split()
    y, m, d = map(int, d_str.split("-"))
    sign = 1 if tz_str[3] == '+' else -1
    hh, mm = map(int, tz_str[4:].split(":"))
    offset = sign * (hh * 3600 + mm * 60)
    return y, m, d, offset

def to_utc_seconds(y, m, d, offset):
    return date(y, m, d).toordinal() * 86400 - offset

def is_leap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

by, bm, bd, birth_off = parse(input())
cy, cm, cd, cur_off = parse(input())

cur_utc = to_utc_seconds(cy, cm, cd, cur_off)

def birthday_utc(year):
    day = bd
    if bm == 2 and bd == 29 and not is_leap(year):
        day = 28
    return to_utc_seconds(year, bm, day, birth_off)

cand1 = birthday_utc(cy)
cand2 = birthday_utc(cy + 1)

target = cand1 if cand1 >= cur_utc else cand2
delta = target - cur_utc

if delta == 0:
    print(0)
else:
    print((delta + 86400 - 1) // 86400)