import json

def parse_query(q):
    tokens = []
    i = 0
    n = len(q)
    while i < n:
        if q[i] == '.':
            i += 1
            continue

        if q[i].isalpha() or q[i] == '_' or q[i].isdigit():
            j = i
            while j < n and q[j] not in '.[':
                j += 1
            tokens.append(("key", q[i:j]))
            i = j
            continue

        if q[i] == '[':
            j = i + 1
            while j < n and q[j] != ']':
                j += 1
            if j == n:
                return None
            idx_str = q[i+1:j]
            if not idx_str.isdigit():
                return None
            tokens.append(("idx", int(idx_str)))
            i = j + 1
            continue

        return None
    return tokens

def resolve(obj, tokens):
    cur = obj
    for typ, val in tokens:
        if typ == "key":
            if isinstance(cur, dict) and val in cur:
                cur = cur[val]
            else:
                return None
        else:
            if isinstance(cur, list) and 0 <= val < len(cur):
                cur = cur[val]
            else:
                return None
    return cur

J = json.loads(input().strip())
q = int(input().strip())

for _ in range(q):
    query = input().strip()
    tokens = parse_query(query)
    if tokens is None:
        print("NOT_FOUND")
        continue

    ans = resolve(J, tokens)
    if ans is None:
        print("NOT_FOUND")
    else:
        print(json.dumps(ans, ensure_ascii=False, separators=(',', ':')))