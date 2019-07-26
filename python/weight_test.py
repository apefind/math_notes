import math
from random import randint
from vector import norm, normed, angle, add, dotprod


def test_weight(x, y):
    print(f"x = {x}, y = {y}")
    print(f"|x| = {norm(x)}, |y| = {norm(y)}")
    print(f"a = {math.degrees(angle(x, y))} deg")
    w = normed(add(normed(x), normed(y)))
    print(f"w = {w}")
    print(f"wx = {dotprod(w, x)}, b = {math.degrees(angle(w, x))} deg")
    print(f"wy = {dotprod(w, y)}, a = {math.degrees(angle(w, y))} deg")
    i, w = 0, x + y
    while True:
        a, b = dotprod(w, x), dotprod(w, y)
        print(f"    w{i} = {w}, w{i} * x = {a}, w{i} * y = {b}")
        # print(f'wx = {dotprod(w, x)}, b = {math.degrees(angle(w, x))} deg')
        # print(f'wy = {dotprod(w, y)}, a = {math.degrees(angle(w, y))} deg')
        if a < 0:
            w = add(w, x)
        elif b < 0:
            w = add(w, y)
        else:
            break
        i = i + 1
    a, b = dotprod(w, x), dotprod(w, y)
    print(f"w / |w| = {w}")
    print(f"w = {w}, w * x = {a}, w * y = {b}")


def get_test_data():
    # return [((-1, 1), (6, 1))]
    return [((4, -6), (-10, 5))]
    n = 10
    return [((randint(-n, n), randint(-n, n)), (randint(-n, n), randint(-n, n))) for _ in range(3)]


if __name__ == "__main__":
    for x, y in get_test_data():
        test_weight(x, y)
