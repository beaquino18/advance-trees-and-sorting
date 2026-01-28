#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time:
        Best case: O(1), constant time, when list is unsorted and we find the problem right away
        Worst case: O(n), linear time, when the list is actually sorted or problem at the very end
        Average case: O(n), linear time
    Memory usage:
        O(1) - constant space
        We only use single variable (index) regardless of input size
        No new arrays or data structures are created
    """
    for index in range(len(items) - 1):
        print(f'Comparing {items[index]} and {items[index + 1]}')
        if items[index] >= items[index + 1]:
            return False
    return True


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
    Running time:
        Best case: O(n²) - Even if array is already sorted, comparison is still needed
        Worst case: O(n²) - When array reversed
        Average case: O(n²) - Random order
    Memory usage:
        O(1) = constant space, the amount of extra memory doesn't depend on # of elements
        """
    # Example array: [9, 4, 5, 7, 1]
    # Repeat the process, each time starting one position further to the right
    # pass = len(items) - 1, since we have 5 elements, we need to do 4 pass
    for index in range(len(items) - 1):
        
        # Assume that the first element in the list is the smallest element so far   
        smallest_index = index
        
        # Compare with rest of unsorted section
        for i in range(index + 1, len(items)):
            if items[i] < items[smallest_index]:
                smallest_index = i
                
        # Swap elements
        items[index], items[smallest_index] = items[smallest_index], items[index]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time:
        Best case: O(n) - Array is already sorted. Each element only needs one comparison (with the element before it), no shifting needed.
        Worst case: O(n²) - Array is reverse sorted. Each element must be compared with and shifted past all elements in the sorted section
        Average case: O(n²) - Random array. On average, each element needs to be compared with about half the sorted section.
    Memory usage:
        O(1) - Constant space
        Only uses a fixed amount of extra variables (current_value, insert_position, loop counters)
        No additional arrays or data structures created
        Memory usage doesn't grow with input size       
    """
    # For each element in the unsorted section:
    #   Remember this element's value
    #   Compare backwards through sorted section
    #   Shift elements as needed
    #   Insert the element to the right spot
    
    # Start with index 1 (index 0 is already "sorted")
    for index in range(1, len(items)):
        # Save the current element we're trying to insert
        current_value = items[index]
        
        # This will track where to insert current_value
        insert_position = index
        
        # Compare backwards through the sorted section
        for j in range(index - 1, -1, -1):
            # If the element is bigger than current_value
            if items[j] > current_value:
                # Shift to the right
                items[j + 1] = items[j]
                #Update where current_value will go
                insert_position = j
            else:
                # Found the right spot, stop searching
                break
        
        # Insert current_value in its correct position
        items[insert_position] = current_value
            



