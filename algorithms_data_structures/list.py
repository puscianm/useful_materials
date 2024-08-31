"""
Lists (abstract data type):

Definition
----------
* collection of items
* finite in number
* in particular order

operations
----------
* create
* test for empty
* add item to beginning or end
* access the first or last item
* accest an item by index
"""

from pprint import pprint as rprint

def print_line(line_len : int):
    rprint("*" * 20 + "" + "*" * 20)

def example():
    print_line(20)

    my_list = [1,2,3, "...", 20, 21]
    rprint(f"This is list: {my_list}")

    not_list = [1,2,3, "..."]
    rprint(f"This is not list: {not_list}")

    print_line(20)

def operations_examples():

    """create"""
    my_list = [1, 2, 3, 4]

    """add item at beginning or end"""
    my_list.insert(0, 0)
    my_list.append(5)
    rprint(my_list)
    
    """access by index"""
    rprint(my_list[3])

    """test for empty"""
    if not my_list:
        rprint("my_list is empty")
    else:
        rprint("my_list is not empty")

if __name__ == "__main__":
    example()
    operations_examples()
