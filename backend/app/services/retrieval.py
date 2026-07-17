import math

def magnitude(vector):
    return math.sqrt(
        sum(x * x for x in vector)
    )

def dot_product(a, b):
    return sum(
        x * y
        for x, y in zip(a, b)
    )

def cosine_similarity(a, b):
    mag_a = magnitude(a)
    mag_b = magnitude(b)

    if mag_a == 0 or mag_b == 0:
        return 0.0

    return (
        dot_product(a, b)
        /
        (mag_a * mag_b)
    )
