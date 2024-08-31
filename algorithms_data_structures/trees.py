"""
Trees:

Definition
----------


operations
----------
* add
* remove
* peek
"""

from pprint import pprint as rprint

def factorial(n):
    print(f"n == {n}")
    if n == 1:
        return 1
    else:
        return(n * factorial(n-1))

def print_line(line_len : int):
    rprint("*" * 20 + "" + "*" * 20)

def binary_search_tree():
    """
    In left node we have strictly lower number than in parent node.
    In right node we have strictly higher number than in parent node
    """
    ...

def AVL_tree():
    """
    It's binary search tree but difference in height between every child subtrees
    differ at moste by one.
    """
    ...

def red_black_tree():
    """
    It's binary search tree but each node has color white or red with these rules:
    ...
    """
    ...

def B_tree():
    """
    Also called ordered binary tree or
    sorted binary tree.


    """
    ...


if __name__ == "__main__":
    print_line(20)
    print(factorial(990))
    print_line(20)
    
