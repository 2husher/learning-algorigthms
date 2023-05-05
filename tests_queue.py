from queue import *

def test_enqueue():
    animals = Queue()
    animals.enqueue("Koala")
    assert animals.first() == "Koala"
    assert animals.count() == 1
    animals.enqueue("Dingo")
    assert animals.first() == "Dingo"
    assert animals.count() == 2

def test_dequeue():
    animals = Queue()
    assert animals.dequeue() == None
    animals.enqueue("Dog")
    animals.enqueue("Cat")
    assert animals.count() == 2
    assert animals.dequeue() == "Dog"
    assert animals.count() == 1
    assert animals.dequeue() == "Cat"
    assert animals.count() == 0
    assert animals.dequeue() == None

def test_first():
    animals = Queue()
    assert animals.first() == None
    animals.enqueue("Hen")
    assert animals.first() == "Hen"
    animals.enqueue("Pig")
    assert animals.first() == "Pig"
    animals.dequeue()
    assert animals.first() == "Pig"

def test_last():
    animals = Queue()
    assert animals.last() == None
    animals.enqueue("Hen")
    assert animals.last() == "Hen"
    animals.enqueue("Pig")
    assert animals.last() == "Hen"
    animals.dequeue()
    assert animals.last() == "Pig"

def test_count():
    animals = Queue()
    assert animals.count() == 0
    animals.enqueue("Hen")
    assert animals.count() == 1
    animals.enqueue("Pig")
    assert animals.count() == 2
    animals.dequeue()
    assert animals.count() == 1
    animals.dequeue()
    assert animals.count() == 0

test_enqueue()
test_dequeue()
test_first()
test_last()
test_count()