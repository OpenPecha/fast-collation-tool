def test_count_weigher():
    cw = TokenCountWeigher()
    assert(cw.weigh(["a", "b", None, "b", "c", None, "a", "b"]) == [25, 37, 25, 37, 12, 25, 25, 37])

if __name__ == "__main__":
    test_count_weigher()