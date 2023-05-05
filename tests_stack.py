from stack import *

def test_push():
    books = Stack()
    assert books.top() == None
    assert books.count() == 0
    books.push("Twilight")
    assert books.top() == "Twilight"
    assert books.count() == 1
    books.push("Hunger Games")
    assert books.top() == "Hunger Games"
    assert books.count() == 2

def test_pop():
    books = Stack()
    assert books.pop() == None
    books.push("Idiot")
    books.push("Iliad")
    assert books.pop() == "Iliad"
    assert books.pop() == "Idiot"
    assert books.pop() == None

def test_top():
    books = Stack()
    assert books.top() == None
    books.push("Idiot")
    assert books.top() == "Idiot"
    books.push("Iliad")
    assert books.top() == "Iliad"
    books.pop()
    assert books.top() == "Idiot"

def test_count():
    books = Stack()
    assert books.count() == 0
    books.push("Idiot")
    assert books.count() == 1
    books.pop()
    assert books.count() == 0




test_push()
test_pop()
test_top()
test_count()
