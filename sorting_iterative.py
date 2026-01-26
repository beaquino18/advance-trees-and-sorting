#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running Time: 
        Worst case (ex. reversed array): O(n^2): quadratic time, as the array gets bigger, the time grows really fast
        Best case (ex. sorted array): O(n): linear time
        Average case (ex. random array): O(n^2), quadratic time, same as worst case
    Memory usage: ??? Why and under what conditions
        O(1): sorts in-place since we're not growing the array size
    """
        
    # Original Array: [10, 7, 1, 3, 6]
    # [7, 10, 1, 3, 6] --> first 0, 1
    # [7, 1, 10, 3, 6] --> index 1, 2
    # Repeat this process until the array is sorted:
    #   Look into the first pair of the array (first and second item on the list)
    #   Compare them using operator > or <
    #   Then move to the second pair (second and third item on the list)
    #   Do this until the items array is sorted
    swapped = True    
    while swapped:
        swapped = False
        for index in range(len(items) - 1):
            if items[index] > items[index + 1]:
                original_value = items[index]
                items[index] = items[index + 1]
                items[index + 1] = original_value
                swapped = True


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
