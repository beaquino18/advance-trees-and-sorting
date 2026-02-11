#!python

from sorting_iterative import insertion_sort;


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n + m) where n = len(items1) and m = len(items2)
        - We iterate through each list exactly once
        - Each comparison and append is O(1)
        - Best, worst, and average are all the same
    Memory time: O(n + m)
        - We create a new list containing all items from both input lists
        - The sorted_list has n + m total items
    """
    # Create empty result list
    sorted_list = []
    
    # # of item in each list
    len1 = len(items1)
    len2 = len(items2)
    
    # Position trackers
    current_position_items1 = 0
    current_position_items2 = 0
    
    # While loop
    while current_position_items1 < len1 and current_position_items2 < len2:
        # Compare the items at current positions & add the smaller one to sorted_list
        if items1[current_position_items1] < items2[current_position_items2]:
            sorted_list.append(items1[current_position_items1])
            current_position_items1 += 1
        else:
            sorted_list.append(items2[current_position_items2])
            current_position_items2 += 1
            
    sorted_list.extend(items1[current_position_items1:])
    sorted_list.extend(items2[current_position_items2:])
    return sorted_list

    
def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time:
        Best case: O(n), linear time when both halves are already sorted
        Worst Case: O(n^2), quadratic time when insertion sort dominates
        Average Case: O(n^2), quadratic time when insertion sort dominates
    Memory usage: O(n)
        - Creating copies of halves: O(n)
        - Merge creates new list: O(n)
        - Insertion sort is in-place: O(1)
    """
    
    # Find the middle of the items array and split
    middle = len(items) // 2
    first_half = items[:middle]
    second_half = items[middle:]
    
    # Sort each half using insertion_sort
    insertion_sort(first_half)
    insertion_sort(second_half)
    
    # Merge the two halves
    return merge(first_half, second_half)
    

    
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    
    Running time: O(n log n) in all cases (best, worst, average)
        - We divide the list log(n) times (splitting in half repeatedly)
        - At each level, we merge n total items
        - Total: n x log(n) comparisons and operations
        - Unlike insertion sort, this is consistent regardless of input order
    
    Memory usage: O(n)
        - Creating new lists during splitting and merging: O(n)
        - Recursion call stack depth: O(log n)
        - Dominated by the O(n) space for list copies
    """
    # Base case - if list is 0 or 1 items, just return it
    if len(items) <= 1:
        return items
    
    # Find middle and split
    middle = len(items) // 2
    first_half = items[:middle]
    second_half = items[middle:]
    
    # Recursively sort each half
    sorted_first_half = merge_sort(first_half)
    sorted_second_half = merge_sort(second_half)
    
    # Merge and return
    return merge(sorted_first_half, sorted_second_half)
    


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Chosen Pivot: Last Element in items
    Running time: O(n) where n = high - low + 1 (the size of the range)
        - We iterate through each item in the range exactly once
        - Each comparison and swap is O(1)
        - Best, worst, and average are all O(n)
    Memory usage: O(1)
        - We only use a constant amount of extra space (pivot, boundary, index)
        - All operations are done in-place on the original list
        - No additional data structures are created
    """
    # Choose a pivot any way and document your method in docstring above
    pivot = items[high]
    
    # Initialize boundary (tracks end of "small items" section)
    boundary = low - 1

    # Loop through all items in range [low...high]
    for index in range(low, high):
        # If current item < pivot:
        #   - Move boundary forward
        #   - Swap current item with item at boundary
        if items[index] < pivot:
            boundary += 1
            items[index], items[boundary] = items[boundary], items[index]
        
    # After loop, place pivot in correct position
    #   - Swap pivot with item at boundary+1
    items[boundary + 1], items[high] = items[high], items[boundary + 1]
    
    # Return the pivot's final index
    return boundary + 1


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Running Time:
        Best Case: O(n log n). The pivot consistently splits the array into roughly equal halves
        Worst Case: O(n^2). Pivot is consistently the smallest or largest element
        Average Case: O(n log n). On random/typical data, pivots are usually good enough
    Memory Usage:
        Best Case: O(log n). Balanced Partitions
        Worst Case: O(log n). Unbalanced
        Average Case: O(n).
    """
    # Check if high and low range bounds have default values (not given)
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1
    
    # Check if list or range is so small it's already sorted (base case)
    if low >= high:
        return
    
    # Partition items in-place around a pivot and get index of pivot
    pivot_index = partition(items, low, high)
    
    # Sort each sublist range by recursively calling quick sort
    quick_sort(items, low, pivot_index - 1)   # Sort left side
    quick_sort(items, pivot_index + 1, high)  # Sort right side
