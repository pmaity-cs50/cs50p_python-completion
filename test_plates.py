# from plates import is_valid

# def test_length():
#     assert is_valid("CS") == True
#     assert is_valid("CS50") == True
#     assert is_valid("CS50P2") == True
#     assert is_valid("H") == False
#     assert is_valid("OUTATIME") == False

# def test_start_with_two_letters():
#     assert is_valid("50") == False
#     assert is_valid("C5") == False
#     assert is_valid("CS") == True

# def test_numbers_placement():
#     assert is_valid("CS50") == True
#     assert is_valid("CS50P") == False
#     assert is_valid("CS05") == False
#     assert is_valid("CS5A") == False

# def test_punctuation():
#     assert is_valid("PI3.14") == False
#     assert is_valid("CS 50") == False
#     assert is_valid("CS!") == False



from plates import is_valid

def test_length():
    assert is_valid("A") == False      # Too short
    assert is_valid("ABCDEFG") == False # Too long
    assert is_valid("AB") == True      # Valid

def test_first_two_letters():
    assert is_valid("A1") == False     # Invalid start
    assert is_valid("1A") == False
    assert is_valid("AB") == True

def test_no_punctuation():
    assert is_valid("AB.CD") == False
    assert is_valid("AB CD") == False

def test_number_placement():
    assert is_valid("ABC12") == True
    assert is_valid("ABC012") == False # Leading zero
    assert is_valid("AB12CD") == False # Numbers in middle
    assert is_valid("AB123") == True

def test_all_numbers():
    assert is_valid("1234") == False   # Fails first-two-letters rule
