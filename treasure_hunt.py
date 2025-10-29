# https://naq25.kattis.com/contests/naq25/problems/treasurehunt2

# Strategy: Check (2, 2), (4, 2), and (4, 4)
# If none hit, implied hit at (2, 4)
# Then, run "localization" pass to find exact coord of chest

def ask(x, y):
    print(f"? {x} {y}")
    return int(input()) == 1

def tell(x, y):
    print(f"! {x} {y}")

def localize(x, y) -> tuple[int, int]:
    is_left = ask(x - 1, y)
    is_above = ask(x, y - 1)

    # Found bottom edge of box
    if is_above:
        y -= 1
    
    # Found right edge of box
    if is_left:
        x -= 1

    return (x, y)

def find() -> tuple[int, int]:

    if (ask(2, 2)):
        return localize(2, 2)

    if (ask(4, 2)):
        return localize(4, 2)

    if (ask(4, 4)):
        return localize(4, 4)

    # None other hit, so implicit hit registered at (2, 4)
    return localize(2, 4)

tell(*find())