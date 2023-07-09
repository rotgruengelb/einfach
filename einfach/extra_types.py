from internals import errors


class Vector:
    def __init__(self, *components: int or float) -> None:
        self._validate_components(components)
        self.components = components

    def _validate_components(self, components) -> None:
        for component in components:
            if not isinstance(component, (int, float)):
                raise TypeError(errors.ERROR_VECTOR_NOT_NUM)

    def __str__(self) -> str:
        return f"Vector({', '.join(str(c) for c in self.components)})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other) -> bool:
        if isinstance(other, Vector):
            return self.components == other.components
        return False

    def __hash__(self):
        return hash(tuple(self.components))

    def __value__(self) -> tuple:
        return self.components


class Color:
    def __init__(self, r: int, g: int, b: int, a: int=255):
        self._validate_component(r)
        self._validate_component(g)
        self._validate_component(b)
        self._validate_alpha(a)
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def _validate_component(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError(errors.ERROR_RGB_COMPO_NOT_INT)
        if value < 0 or value > 255:
            raise ValueError(errors.ERROR_RGB_COMPO_OUT_RANGE)

    def _validate_alpha(self, value) -> None:
        if not isinstance(value, int):
            raise TypeError(errors.ERROR_A_COMPO_NOT_INT)
        if value < 0 or value > 255:
            raise ValueError(errors.ERROR_A_COMPO_OUT_RANGE)

    def __str__(self, force_rgba: bool=False) -> str:
        if self.a == 255 and force_rgba is not True:
            return f"RGB({self.r}, {self.g}, {self.b})"
        else:
            return f"RGBA({self.r}, {self.g}, {self.b}, {self.a})"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other) -> bool:
        if isinstance(other, Color):
            return (
                    self.r == other.r
                and self.g == other.g
                and self.b == other.b
                and self.a == other.a
            )
        return False

    def __hash__(self):
        return hash((self.r, self.g, self.b, self.a))

    def as_rgb(self) -> tuple:
        return self.r, self.g, self.b

    def __value__(self) -> tuple:
        return self.r, self.g, self.b, self.a
    def as_rgba(self) -> tuple: # Alias
        return self.__value__()
