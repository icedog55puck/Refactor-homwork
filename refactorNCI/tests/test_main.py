import sys
sys.path.append("./refactornci")
from main import * 
from main import Node
from main import DoublyLinkedList

def test_no_shit():
    assert 1 == 1 + 0 

def test_add():
    node = Node(1)
    assert str(node) == "(1, None)"
def test_DLL():
    dL = DoublyLinkedList()

    for i in range(4):
        dL.add_last(Node(i))

    print(dL)

    assert str(dL) == f"(0, (1, (2, (3, ('Trailer', None)))))"  

# Task 2: Test the size method
def test_size():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    assert dL.size() == 4

# Task 3: Test the is_empty method
def test_is_empty():
    dL = DoublyLinkedList()
    assert dL.is_empty() == True

    for i in range(4):
        dL.add_last(Node(i))
    
    assert dL.is_empty() == False

# Task 4: Test the get_first and get_last methods
def test_get_first_and_get_last():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    
    assert str(dL.get_first()) == f"(0, (1, (2, (3, ('Trailer', None)))))"
    assert str(dL.get_last()) == f"(3, ('Trailer', None))"

# Task 5: Test the get_previous and get_next methods
def test_get_previous_and_get_next():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    
    assert str(dL.get_last().get_previous()) == "(2, (3, ('Trailer', None)))"
    assert str(dL.get_first().get_next()) == "(1, (2, (3, ('Trailer', None))))"

# Task 6: Test the add_before and add_after methods
def test_add_before_and_add_after():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))

    dL.add_after(Node(42), dL.get_first())
    dL.add_before(Node(34), dL.get_last())
    
    assert str(dL) == "(0, (42, (1, (2, (34, (3, ('Trailer', None)))))))"

# Task 7: Test the add_first and add_last methods
def test_add_first_and_add_last():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))

    dL.add_first(Node(7))
    dL.add_last(Node(-1))

    assert str(dL) == "(7, (0, (1, (2, (3, (-1, ('Trailer', None)))))))"

# Task 8: Test the remove method
def test_remove():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    
    dL.remove(dL.get_first())
    assert dL.get_first().get_element() == 1

# Task 9: Test the map method
def test_map():
    dL = DoublyLinkedList()
    for i in range(4):
        dL.add_last(Node(i))
    
    dL.map(lambda x: x ** 2)
    
    assert str(dL) == "(0, (1, (4, (9, ('Trailer', None)))))"

