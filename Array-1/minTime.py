# Given an integer array A of size N. In one second, you can increase the value of one element by 1.
# Find the minimum time in seconds to make all elements of the array equal.

def min_time_to_equal(A):
    max_element = max(A)
    total_time = 0
    for num in A:
        total_time += max_element - num
    return total_time

A = [2, 4, 1, 3, 2]

print(f"Min time to equal: {min_time_to_equal(A)}")