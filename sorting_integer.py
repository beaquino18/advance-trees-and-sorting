#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time:
        - O(n + k) where n is the count of numbers and k is the range of 
        values (max - min). We loop over all n numbers to count them, then loop
        over k slots in the count array to build the output.
        
    Memory usage:
        - O(k) where k is the range of values (max - min). We create a count 
        array with one slot for each value in the range, regardless of how many
        numbers are in the input.
    """
    # Find range of given numbers (minimum and maximum integer values)
    min_number = min(numbers)
    max_number = max(numbers)
    
    # Create list of counts with a slot for each number in input range
    count_array = [0] * (max_number + 1 - min_number)
    
    # Loop over given numbers and increment each number's count
    for values in numbers:
        index = values - min_number
        count_array[index] += 1
    
    # Loop over counts and append that many numbers into output list
    i = 0
    for index in range(len(count_array)):
        count = count_array[index]
        while count > 0:
            numbers[i] = index + min_number
            i += 1
            count -= 1
    
    return numbers


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
