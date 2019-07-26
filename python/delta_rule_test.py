from delta_rule import dotprod, delta_rule


def heaviside(x):
    return 0 if x < 0.0 else 1


def and_(x, y):
    return int(x and y)


def or_(x, y):
    return int(x or y)


def xor(x, y):
    return int(x and not y or not x and y)


def nand(x, y):
    return int(not x and not y)


def test_delta_rule(f, X, a, da):
    T = [(x, f(*x)) for x in X]
    w, b = delta_rule(T, a, da)
    p = lambda x: 0 if dotprod(w, x) + b < 0.5 else 1
    for x, y in T:
        print(f"{f.__name__}{x} -> {p(x)}: {y}")
    print(f"{f.__name__}: {all(p(x) == y for x, y in T)}")


if __name__ == "__main__":
    a, da = lambda x: x, lambda x: 1
    X = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for f in (or_, and_, nand, xor):
        test_delta_rule(f, X, a, da)
