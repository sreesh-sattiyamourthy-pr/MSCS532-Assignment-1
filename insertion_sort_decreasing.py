# ==============================================================================
# Project: MSCS532 Assignment 1 - Insertion Sort Algorithm (Monotonically Decreasing)
# Author: Sresh
# Date: 2025-10-25
# Description:
# This program implements the Insertion Sort algorithm to sort a list of numbers
# in monotonically decreasing order. The Insertion Sort algorithm works by
# iteratively inserting each element from an unsorted portion of the list into 
# its correct position in the sorted portion of the list.
# The goal of this project is to demonstrate the concept of sorting algorithms 
# and to practice using version control through GitHub.
# 
# ==============================================================================
 
def insertion_sort(arr):
    """
    Performs Insertion Sort on the given array in monotonically decreasing order.

    :param arr: List of elements to be sorted
    :return: The sorted list in decreasing order
    """
    # Traverse through the array starting from the second element
    # because the first element is trivially "sorted"
    for i in range(1, len(arr)):
        # Store the current element to be inserted into the sorted portion of the list
        key = arr[i]
        
        # Initialize the index 'j' to the element just before the current element
        j = i - 1
        
        # Move elements of arr[0..i-1], that are smaller than 'key', to one position ahead
        # of their current position, to make space for the 'key' in the sorted portion
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1  # Move the pointer to the left

        # Place the 'key' in the correct position in the sorted portion of the array
        arr[j + 1] = key

    # Return the sorted array
    return arr

# ==============================================================================
# Test the Insertion Sort Algorithm
# ==============================================================================
if __name__ == "__main__":
    # Sample input array to demonstrate sorting
    arr = [12, 11, 13, 5, 6]
    
    # Print the original array before sorting
    print("Original Array:", arr)
    
    # Call the insertion_sort function to sort the array in decreasing order
    sorted_arr = insertion_sort(arr)
    
    # Print the sorted array
    print("Sorted Array (Monotonically Decreasing):", sorted_arr)

# ==============================================================================
# Expected Output:
# Original Array: [12, 11, 13, 5, 6]
# Sorted Array (Monotonically Decreasing): [13, 12, 11, 6, 5]
# ==============================================================================
