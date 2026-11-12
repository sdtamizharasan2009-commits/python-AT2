import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200000)]


def build_plus(parts):
    text = ""

    for p in parts:
        text += p + ";"

    return text


def build_join(parts):
    return "".join(p + ";" for p in parts)


def build_fstring(parts):
    return "".join(f"{p};" for p in parts)


for count in [1000, 10000, 200000]:
    data = items[:count]

    start = time.perf_counter()
    a = build_plus(data)
    t_plus = time.perf_counter() - start

    start = time.perf_counter()
    b = build_join(data)
    t_join = time.perf_counter() - start

    start = time.perf_counter()
    c = build_fstring(data)
    t_fstring = time.perf_counter() - start

    print("Number of lines:", count)
    print("Same text:", a == b == c)
    print(f"+= time: {t_plus:.4f} s")
    print(f"join time: {t_join:.4f} s")
    print(f"f-string time: {t_fstring:.4f} s")