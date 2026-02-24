import math

def dist(x, y):
    return math.hypot(x, y)

def seg_distance_to_origin(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    a = dx*dx + dy*dy
    if a == 0.0:
        return dist(x1, y1)
    t = -(x1*dx + y1*dy) / a
    if t < 0.0:
        return dist(x1, y1)
    if t > 1.0:
        return dist(x2, y2)
    px = x1 + t*dx
    py = y1 + t*dy
    return dist(px, py)

def ang_norm(a):
    two_pi = 2.0 * math.pi
    a %= two_pi
    if a < 0:
        a += two_pi
    return a

def ang_diff(a, b):
    two_pi = 2.0 * math.pi
    d = abs(ang_norm(a) - ang_norm(b))
    return min(d, two_pi - d)

R = float(input().strip())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

eps = 1e-12

dmin = seg_distance_to_origin(x1, y1, x2, y2)
straight = math.hypot(x2 - x1, y2 - y1)

if dmin >= R - 1e-12:
    print(f"{straight:.10f}")
else:
    r1 = dist(x1, y1)
    r2 = dist(x2, y2)

    angA = math.atan2(y1, x1)
    angB = math.atan2(y2, x2)

    a1 = 0.0 if abs(r1 - R) <= eps else math.acos(R / r1)
    a2 = 0.0 if abs(r2 - R) <= eps else math.acos(R / r2)

    tA = [angA + a1, angA - a1]
    tB = [angB + a2, angB - a2]

    lenA = 0.0 if abs(r1 - R) <= eps else math.sqrt(r1*r1 - R*R)
    lenB = 0.0 if abs(r2 - R) <= eps else math.sqrt(r2*r2 - R*R)

    best = float("inf")
    for ta in tA:
        for tb in tB:
            phi = ang_diff(ta, tb)
            cand = lenA + lenB + R * phi
            if cand < best:
                best = cand

    print(f"{best:.10f}")