def normalise(text):
    return text.replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    if not reg[:2].isalpha():
        return False

    if not reg[2:4].isdigit():
        return False

    if not (reg[4:-4].isalpha() and 1 <= len(reg[4:-4]) <= 2):
        return False

    if not reg[-4:].isdigit():
        return False

    return True


def format_number(reg):
    if is_valid(reg):
        return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]
    return "INVALID"


numbers = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "KL 07 CD 5678",
    "AP-39-XY-1234"
]

for raw in numbers:
    reg = normalise(raw)
    print(f"{raw:15} -> {reg:11} {'valid' if is_valid(reg) else 'INVALID'}")

    if is_valid(reg):
        print(format_number(reg))