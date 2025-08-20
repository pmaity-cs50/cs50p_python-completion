# from numb3rs import validate

# def test_valid_ip():
#     assert validate("127.0.0.1") == True
#     assert validate("255.255.255.255") == True
#     assert validate("0.0.0.0") == True

# def test_invalid_range():
#     assert validate("256.0.0.0") == False
#     assert validate("1.2.3.256") == False
#     assert validate("-1.0.0.0") == False

# def test_invalid_format():
#     assert validate("1.2.3") == False
#     assert validate("1.2.3.4.5") == False
#     assert validate("cat.dog.bird.mouse") == False
#     assert validate("1.2.3,4") == False

# def test_invalid_zeroes():
#     assert validate("0.1.2.3") == True
#     assert validate("00.1.2.3") == True



from numb3rs import validate

def test_valid_ip():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid_range():
    assert validate("256.0.0.0") == False
    assert validate("1.2.3.256") == False
    assert validate("-1.0.0.0") == False

def test_invalid_format():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("cat.dog.bird.mouse") == False
    assert validate("1.2.3,4") == False

def test_leading_zeros():
    assert validate("000.001.010.100") == False
    assert validate("00.1.2.3") == False
