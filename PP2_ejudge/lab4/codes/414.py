from datetime import date

def parse(line: str) -> int:
    d_str, tz_str = line.strip().split()
    y, m, d = map(int, d_str.split("-"))

    sign = 1 if tz_str[3] == '+' else -1
    hh, mm = map(int, tz_str[4:].split(":"))
    offset = sign * (hh * 3600 + mm * 60)

    days = date(y, m, d).toordinal()
    return days * 86400 - offset

t1 = parse(input())
t2 = parse(input())

diff = abs(t1 - t2)
print(diff // 86400)