import json

MISSING = object()

def compact(v):
    # value-ді compact JSON literal түрінде шығару
    return json.dumps(v, ensure_ascii=False, separators=(',', ':'), sort_keys=True)

def diff(a, b, path="", out=None):
    if out is None:
        out = []

    # Екеуі де dict болса — key-лердің біріккен жиыны бойынша жүріп өтеміз
    if isinstance(a, dict) and isinstance(b, dict):
        keys = set(a.keys()) | set(b.keys())
        for k in keys:
            new_path = f"{path}.{k}" if path else k
            av = a.get(k, MISSING)
            bv = b.get(k, MISSING)

            if av is MISSING:
                out.append((new_path, "<missing>", compact(bv)))
            elif bv is MISSING:
                out.append((new_path, compact(av), "<missing>"))
            else:
                # екеуі де бар
                if isinstance(av, dict) and isinstance(bv, dict):
                    diff(av, bv, new_path, out)
                else:
                    if av != bv:
                        out.append((new_path, compact(av), compact(bv)))
        return out

    # Егер dict емес деңгейге түсіп кетсе (әдетте болмайды, бірақ safe)
    if a != b:
        left = "<missing>" if a is MISSING else compact(a)
        right = "<missing>" if b is MISSING else compact(b)
        out.append((path if path else "", left, right))
    return out


A = json.loads(input().strip())
B = json.loads(input().strip())

changes = diff(A, B)
changes.sort(key=lambda x: x[0])

if not changes:
    print("No differences")
else:
    for p, old, new in changes:
        print(f"{p} : {old} -> {new}")