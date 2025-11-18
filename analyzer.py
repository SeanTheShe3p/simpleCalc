import pytest
from collections import Counter
import test_analyzer


def count_words(text):
    i = 0
    for each in text:
        i = i + 1
    return i
def count_chars(text):
    if text == "":
        return 0
    i = 0
    for each in text:
         for char in each:
            i = i + 1
    return i

def find_most_common_word(text):
    words = text.split()
    if not words:
        return None
    word_counts = Counter(words)
    most_common_word, _ =  word_counts.most_common(1)[0]
    return most_common_word



if __name__ == "__main__":
    print(find_most_common_word("The imaginary fox fox"))