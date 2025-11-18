import pytest

def add_two_numbers(x, y):
    return x + y

def multiply_two_numbers(x, y):
    return x * y

def subtract_two_numbers(X, y):
    return X - y

def divide_two_numbers(x, y):
    return x / y

def test_add_two_numbers():
    assert add_two_numbers(2,4) == 6

def test_multiply_two_numbers():
    assert multiply_two_numbers(2,4) == 8

def test_subtract_two_numbers():
    assert subtract_two_numbers(4,2) == 2

def test_divide_two_numbers():
    assert divide_two_numbers(4,2) == 2

if __name__ == "__main__":
    option = input("file option:\nAdd - 1\nSub - 2\n Multi - 3\nDiv - 4")
    number1 = input("what numbers?\nnumber1?")
    number2 = input("number2?")
    if(option == 1):
        print(add_two_numbers(number1,number2))   
    if(option == 2):
        print(add_two_numbers(number1,number2))
    if(option == 3):
        print(add_two_numbers(number1,number2))
    if(option == 4):
        print(add_two_numbers(number1,number2))