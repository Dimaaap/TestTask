import pytest
from positive_integer import A


class TestA:

    def test_number_assignment(self):
        a = A()

        a.number = 1
        assert a.number == 1, "Failed in assignment"

    def test_invalid_assignment(self):
        a = A()

        with pytest.raises(TypeError, match="Expected an integer, got str"):
            a.number = "test string"

    def test_number_assignment_after_invalid(self):
        a = A()

        a.number = 10
        assert a.number == 10, "Number != 10"

        with pytest.raises(TypeError, match="Expected an integer, got str"):
            a.number = "invalid string"

    def test_delete_number(self):
        a = A()

        a.number = 5
        assert a.number == 5
        del a.number

        with pytest.raises(AttributeError):
            print(a.number)

