# from bank import value

# def test_zero():
#     assert value("hello") == 0
#     assert value("Hello, Newman") == 0
#     assert value("HeLLo") == 0

# def test_twenty():
#     assert value("how you doing?") == 20
#     assert value("Hey there") == 20
#     assert value("H") == 20

# def test_one_hundred():
#     assert value("good morning") == 100
#     assert value("What's up?") == 100
#     assert value("C") == 100



from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO there") == 0

def test_h_but_not_hello():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("H") == 20

def test_other():
    assert value("what's up") == 100
    assert value("good morning") == 100
    assert value("123") == 100
