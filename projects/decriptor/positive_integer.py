class PositiveInteger:

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if isinstance(value, int):
            self._value = value
        else:
            raise TypeError(f"Expected an integer, got {type(value).__name__}")

    def __delete__(self, instance):
        del self._value


class A:
    number = PositiveInteger()

