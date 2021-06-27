import pytest
import math
from factorial_example import factorial_function

def test_factorial_functionality():
    print("Inside test_factorial_functionality")

    assert factorial_function(0) == 1
    assert factorial_function(4) == 24

def test_standard_library():
    print("Inside test dtandard library")

    for i in range(5):
        assert math.factorial(i) == factorial_function(i)

def test_negative_number():
    print("Inside test_neagative_number")

    with pytest.raises(AssertionError):
        factorial_function(-10)

