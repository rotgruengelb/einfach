from extra_types import Vector, Color
from einfach.internals import errors


def vec_to_rgba(vector: Vector):
    try:
        if vector.components[4]: raise ValueError(errors.ERROR_VECTOR_NOT_VEC4)
    except IndexError: pass
    try:
        a = int(vector.components[3] * 255)
    except IndexError: a = 255
    return Color(
            r = int(vector.components[0] * 255),
            g = int(vector.components[1] * 255),
            b = int(vector.components[2] * 255),
            a = a )
