import pytest
import math_function
import sys


@pytest.mark.parametrize(
    argnames="number1, number2, result",
    argvalues=[
        (1, 5, 6), 
        ("Hello ", "Zaydoun", "Hello Zaydoun"), 
        (10.4, 10.2, 20.6)],
)
def test_add(number1, number2, result):
    assert math_function.add(number1, number2) == result


# @pytest.mark.number
# def test_add():
#    """
#    Tests the addition  of 2 integers
#    """
#    print("Testing the function of calculating the sum of 2 numbers")
#    assert math_function.add(1, 2) == 3
#    assert math_function.add(2, 2) == 4


@pytest.mark.number
# @pytest.mark.skip(reason="Already Tested")
def test_product():
    """
    Tests the product of 2 numbers

    """
    print("Testing the function of calculating the product of 2 numbers")
    assert math_function.product(1, 2) == 2
    assert math_function.product(2.2, 2) == 4.4


@pytest.mark.skipif(
    sys.version_info < (3, 11, 4), reason="requires python 3.11.4 or higher"
)
def test_add_strings():
    """
    Tests the addition of 2 strings
    """
    print("Testing the function of adding 2 strings")
    concatenated = math_function.add("Hello Zied", "MLOps")
    assert concatenated == "Hello ZiedMLOps"
    assert "Hello" in concatenated, f"Hello is not present in {concatenated}"
    assert isinstance(
        concatenated, str
    ), f"Expected an str type of the result but got {type(concatenated)} instead"
