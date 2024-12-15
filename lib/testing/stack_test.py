import pytest  # Import pytest

from Stack import Stack

class TestStack:
    '''Class Stack in Stack.py'''

    def test_init(self):
        '''Initialize Stack with list'''
        stk = Stack([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        for index in range(len(expected)):
            assert(expected[index] == stk.stack[index])  # Use stk.stack instead of stk.items

    def test_push(self):
        '''Push 0 to stack'''
        stk = Stack([1, 2, 3, 4, 5])
        stk.push(0)
        expected = [1, 2, 3, 4, 5, 0]
        for index in range(len(expected)):
            assert(expected[index] == stk.stack[index])  # Use stk.stack instead of stk.items

    def test_pop(self):
        '''Pop 1 off the stack'''
        stk = Stack([1, 2, 3, 4, 5])
        stk.pop()
        expected = [1, 2, 3, 4]
        for index in range(len(expected)):
            assert(expected[index] == stk.stack[index])  # Use stk.stack instead of stk.items

    def test_size(self):
        '''Test Stack size() method'''
        stk = Stack([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        assert(stk.size() == len(expected))

    def test_empty(self):
        '''Test Stack empty() method'''
        stk = Stack()
        assert(stk.isEmpty())
        assert(stk.size() == 0)
        with pytest.raises(IndexError):  # Popping from an empty stack should raise an error
            stk.pop()  # This will raise an IndexError when the stack is empty
        stk.push(1)
        assert(not stk.isEmpty())
        assert(stk.size() == 1)
        assert(stk.pop() == 1)

    def test_full(self):
        '''Test Stack full() method'''
        stk = Stack([1], 1)  # stack with one item and limit of 1
        
        assert(stk.full())
        assert(stk.size() == 1)
        assert(stk.pop() == 1)
        stk.push(1)
        with pytest.raises(IndexError):  # Stack should be full, cannot push another item
            stk.push(2)

    def test_search(self):
        '''Test Stack search() method. How far is the element in the stack? '''
        stk = Stack([5, 6, 7, 8, 9, 10])

        assert(stk.search(5) == 5)  # Element is 5 items from the top
        assert(stk.search(6) == 4)  # Element is 4 items from the top
        assert(stk.search(7) == 3)  # Element is 3 items from the top
        assert(stk.search(8) == 2)  # Element is 2 items from the top
        assert(stk.search(9) == 1)  # Element is 1 item from the top
        assert(stk.search(10) == 0)  # Element is at the top

        # Case with target not in Stack
        assert(stk.search(15) == -1)  # Element is not in the stack
