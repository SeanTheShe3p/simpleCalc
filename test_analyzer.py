from analyzer import count_words, count_chars, find_most_common_word 
def test_count_words():
    assert count_words(["apple", "bannana"]) == 2
def test_count_chars():
    assert count_chars("list") == 4
def test_find_most_common_word():
    assert find_most_common_word("the task task is fresh") == "task"
def test_count_words_1():
    assert count_words([]) == 0
def test_count_chars_1():
    assert count_chars("") == 0
def test_most_common_word_1():
    assert find_most_common_word("") == None
def test_most_common_word2():
    assert find_most_common_word("book book book") == "book"