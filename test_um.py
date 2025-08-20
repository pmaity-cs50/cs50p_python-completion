from um import count

def test_um_case_insensitive():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um, thanks for the um.") == 2

def test_um_whole_word():
    assert count("um, um...") == 2
    assert count("yummy um") == 1
    assert count("Yummy, um...") == 1
    assert count("Album") == 0

def test_um_with_punctuation():
    assert count("um?") == 1
    assert count("Um...") == 1
    assert count("um, um, um,") == 3

def test_no_um():
    assert count("Hello, world") == 0
