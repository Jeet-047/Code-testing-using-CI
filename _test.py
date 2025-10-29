import pytest

# Define functions
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def fifth_power(x):
    return x** 5

# Now test each individual functions
def test_square():
    assert square(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square(3) == 9, "Test Failed: Square of 3 should be 9"

def test_cube():
    assert cube(2) == 8, "Test Failed: Cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: Cube of 3 should be 27"

def test_fifth_power():
    assert fifth_power(2) == 32, "Test Failed: 5th power of 2 should be 32"
    assert fifth_power(3) == 243, "Test Failed: 5th power of 3 should be 243"

# Test for individual input
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")
        cube("string")
        fifth_power("string")