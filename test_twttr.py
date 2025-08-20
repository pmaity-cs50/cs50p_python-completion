from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("123, abc!") == "123, bc!"
    assert shorten("aeiouAEIOU") == ""

if __name__ == "__main__":
    main()
