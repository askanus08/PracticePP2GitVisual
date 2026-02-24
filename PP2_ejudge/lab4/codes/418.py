x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

x = x1 + (x2 - x1) * (y1 / (y1 + y2))
print(f"{x:.10f} {0.0:.10f}")