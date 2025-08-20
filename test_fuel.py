# import pytest
# from fuel import convert, gauge

# def test_convert_valid_fractions():
#     assert convert("1/4") == (1, 4)
#     assert convert("3/4") == (3, 4)
#     assert convert("99/100") == (99, 100)

# def test_convert_errors():
#     with pytest.raises(ZeroDivisionError):
#         convert("1/0")
#     with pytest.raises(ValueError):
#         convert("1.5/3")
#     with pytest.raises(ValueError):
#         convert("4/3")
#     with pytest.raises(ValueError):
#         convert("cat/dog")

# def test_gauge():
#     assert gauge(1, 100) == "E"
#     assert gauge(0, 100) == "E"
#     assert gauge(99, 100) == "F"
#     assert gauge(100, 100) == "F"
#     assert gauge(1, 2) == "50%"import pytest
# from fuel import convert, gauge

# def test_convert_valid_fractions():
#     assert convert("1/4") == (1, 4)
#     assert convert("3/4") == (3, 4)
#     assert convert("99/100") == (99, 100)

# def test_convert_errors():
#     with pytest.raises(ZeroDivisionError):
#         convert("1/0")
#     with pytest.raises(ValueError):
#         convert("1.5/3")
#     with pytest.raises(ValueError):
#         convert("4/3")
#     with pytest.raises(ValueError):
#         convert("cat/dog")

# def test_gauge():
#     assert gauge(1, 100) == "E"
#     assert gauge(0, 100) == "E"
#     assert gauge(99, 100) == "F"
#     assert gauge(100, 100) == "F"
#     assert gauge(1, 2) == "50%"


from fuel import convert, gauge
import pytest

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    assert convert("3/4") == 75

def test_convert_errors():
    with pytest.raises(ValueError):
        convert("3/2")  # X > Y
    with pytest.raises(ValueError):
        convert("cat/dog")  # Non-integers
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Zero division
    with pytest.raises(ValueError):
        convert("-1/5")  # Negative numbers

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
