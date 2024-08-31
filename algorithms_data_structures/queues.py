"""
queue (abstract data type):

Definition
----------
Basically a stack only pop operation is being done not at the "top" but at the bottom.

Implemented as doubly/signly linked list or modified dynamic array 

operations
----------
* push (at the top of the queue)
* pop (from the bottom of the queue)
* peek (return value of bottom element without modifying dequeueing)
"""

from pprint import pprint as rprint

def print_line(line_len : int):
    rprint("*" * 20 + "" + "*" * 20)

def example():
    print_line(20)

    my_str = """
                                                            POINTER TO HEAD
                                                                 |
                                                                 |
                                                                 |
                                                                 |
                                                                \!/
    [[1, 2000], [2, 2004], [3, 2008], [4, 2012], [5, 2016], [6, 2020]]"""
    print(my_str)


    print_line(20)

def operations_examples():

    my_list = []
    """enqueue"""
    my_list.append("zero")
    rprint(f"enqueued : {my_list[-1]}")
    my_list.append("one")
    rprint(f"enqueued : {my_list[-1]}")
    my_list.append("two")
    rprint(f"enqueued : {my_list[-1]}")
    
    rprint(my_list)
    
    """dequeue"""
    rprint(f"dequeued : {my_list.pop(0)}")

    rprint(f"dequeued : {my_list.pop(0)}")

if __name__ == "__main__":
    example()
    operations_examples()
