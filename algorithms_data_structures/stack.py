"""
stack (abstract data type):

Definition
----------
Basically a list or an array. Only distinction from them is the interface which user has.
User can only perform operation on the last element -- push and pop.

operations
----------
* push (at the top of the stack)
* pop (from the top of the stack)
* peek (return value of last element added without modifying stack)
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
    """push"""
    my_list.append("zero")
    my_list.append("two")
    my_list.append("three")
    rprint(my_list)
    
    """pop"""
    rprint(f"popped : {my_list.pop()}")

    rprint(f"popped : {my_list.pop()}")

if __name__ == "__main__":
    example()
    operations_examples()
