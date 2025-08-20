# # # import pytest
# # # from seasons import calculate_minutes

# # # def test_calculate_minutes():

# # #     assert calculate_minutes("2024-01-01") == 3270600

# # # def test_invalid_date():
# # #     with pytest.raises(ValueError):
# # #         calculate_minutes("12-1-2022")
# # #     with pytest.raises(ValueError):
# # #         calculate_minutes("2022-13-01")
# # #     with pytest.raises(ValueError):
# # #         calculate_minutes("2022-01-32")

# # # def test_future_date():
# # #     with pytest.raises(ValueError):
# # #         calculate_minutes("2030-01-01")


# # import pytest
# # from seasons import calculate_minutes

# # def test_calculate_minutes():
# #     # Test a known date difference
# #     # The actual value for a date in the past will be different for check50's "today"
# #     # So we'll trust that the function works correctly with a single known date
# #     assert calculate_minutes("2024-01-01") == 3270600

# # def test_invalid_date():
# #     with pytest.raises(ValueError):
# #         calculate_minutes("12-1-2022")
# #     with pytest.raises(ValueError):
# #         calculate_minutes("2022-13-01")
# #     with pytest.raises(ValueError):
# #         calculate_minutes("2022-01-32")

# # def test_future_date():
# #     with pytest.raises(ValueError):
# #         calculate_minutes("2030-01-01")


# # import pytest
# # import sys
# # from seasons import calculate_minutes, main

# # def test_calculate_minutes():
# #     # Test a known date difference
# #     # The actual value for a date in the past will be different for check50's "today"
# #     # So we'll trust that the function works correctly with a single known date
# #     assert calculate_minutes("2024-01-01") == 3270600

# # def test_invalid_date():
# #     with pytest.raises(ValueError):
# #         calculate_minutes("12-1-2022")
# #     with pytest.raises(ValueError):
# #         calculate_minutes("2022-13-01")
# #     with pytest.raises(ValueError):
# #         calculate_minutes("2022-01-32")

# # def test_future_date():
# #     with pytest.raises(ValueError):
# #         calculate_minutes("2030-01-01")




# from seasons import get_minutes_lived, number_to_words
# import pytest
# from datetime import date

# def test_get_minutes_lived():
#     # Test for a birthdate one year ago
#     birthdate = date(2022, 1, 1)
#     assert get_minutes_lived(birthdate) == 525600

#     # Test for a birthdate two years ago
#     birthdate = date(2021, 1, 1)
#     assert get_minutes_lived(birthdate) == 1051200

# def test_number_to_words():
#     assert number_to_words(0) == "zero"
#     assert number_to_words(1) == "one"
#     assert number_to_words(525600) == "five hundred twenty-five thousand, six hundred"

# def test_invalid_date():
#     with pytest.raises(SystemExit):
#         get_minutes_lived(date(2024, 2, 30))  # Invalid date (February has 28 or 29 days)



from seasons import get_date, calculate_minutes, convert_to_words
from datetime import date
import pytest

def test_get_date_valid():
    assert get_date("2000-01-01") == date(2000, 1, 1)

def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("January 1, 2000")
    with pytest.raises(ValueError):
        get_date("2000-13-01")

def test_calculate_minutes():
    assert calculate_minutes(date(2000, 1, 1), date(2000, 1, 2)) == 1440
    with pytest.raises(ValueError):
        calculate_minutes(date(2025, 1, 1), date(2024, 1, 1))

def test_convert_to_words():
    assert convert_to_words(1440) == "One thousand, four hundred forty minutes"
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
