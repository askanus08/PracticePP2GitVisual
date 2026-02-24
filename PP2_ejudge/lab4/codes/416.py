import math

R = float(input().strip())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

a = dx*dx + dy*dy
seg_len = math.sqrt(a)

def out(val):
    print(f"{val:.10f}")

if a == 0.0:
    out(0.0)
else:
    b = 2.0 * (x1*dx + y1*dy)
    c = x1*x1 + y1*y1 - R*R
    disc = b*b - 4.0*a*c

    eps = 1e-12
    if disc < -eps:
        out(seg_len if c <= 0.0 else 0.0)
    else:
        if disc < 0.0:
            disc = 0.0
        s = math.sqrt(disc)
        t1 = (-b - s) / (2.0 * a)
        t2 = (-b + s) / (2.0 * a)
        if t1 > t2:
            t1, t2 = t2, t1

        left = max(0.0, t1)
        right = min(1.0, t2)
        inside = max(0.0, right - left)

        out(inside * seg_len)