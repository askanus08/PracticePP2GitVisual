import json

def apply_patch(source, patch):
    for k, v in patch.items():
        if v is None:
            source.pop(k, None)  # remove key if exists
        else:
            if k in source and isinstance(source[k], dict) and isinstance(v, dict):
                apply_patch(source[k], v)  # recursive
            else:
                source[k] = v  # add or replace
    return source

source = json.loads(input().strip())
patch = json.loads(input().strip())

result = apply_patch(source, patch)
print(json.dumps(result, sort_keys=True, separators=(',', ':')))