"""
Linked list

Definition
----------
linear collection of nodes. Each node containing data and link
to the next node. Last node contains link to terminator

operations
----------
* access (end) - O(n) if unknown end element
* access (beginning) - O(1)
* access (middle) - O(n)
* peek by index - O(n)
"""

from pprint import pprint as rprint

def print_line(line_len : int):
    rprint("*" * 20 + "" + "*" * 20)

def example():
    print_line(20)

    my_linked_list = [[5, '0xb73eb000'], [7, '0xb73eb010'], [9, '0xb73eb030'], [11, '0xb73eb020']]
    rprint(f"This is linked list: {my_linked_list}")

    print_line(20)

if __name__ == "__main__":
    example()
