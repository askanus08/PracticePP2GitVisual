import importlib

q = int(input().strip())

for _ in range(q):
    module_path, attr = input().split()
    try:
        mod = importlib.import_module(module_path)
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
        continue

    if not hasattr(mod, attr):
        print("ATTRIBUTE_NOT_FOUND")
        continue

    val = getattr(mod, attr)
    print("CALLABLE" if callable(val) else "VALUE")