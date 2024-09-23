def bubble_sort_count(arr, ascending=True):
    """
    Counts the number of swaps needed to sort an array using Bubble Sort.

    Args:
    arr (list): The array of integers to be sorted.
    ascending (bool): True to sort in ascending order, False for descending.

    Returns:
    int: The number of swaps performed.
    """
    swap_count = 0
    n = len(arr)
    
    # Bubble Sort with a swap counter
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
                swapped = True
        # If no swaps in this pass, array is already sorted
        if not swapped:
            break
    return swap_count

def minimum_swaps_to_beautiful(arr):
    """
    Determines the minimum number of swaps required to make the array beautiful.
    A beautiful array is sorted in either ascending or descending order.

    Args:
    arr (list): The input array of integers.

    Returns:
    int: The minimum number of swaps to make the array beautiful.
    """
    if len(arr) <= 1:
        return 0  # Edge case: an empty or single-element array is already beautiful

    # Create separate copies for sorting both ways
    asc_arr = arr[:]
    desc_arr = arr[:]

    # Count swaps for ascending and descending
    asc_swaps = bubble_sort_count(asc_arr, ascending=True)
    desc_swaps = bubble_sort_count(desc_arr, ascending=False)

    # Return the minimum number of swaps required
    return min(asc_swaps, desc_swaps)

# Main Function to handle input and output
if __name__ == "__main__":
    # Input reading
    n = int(input())  # Read number of elements
    arr = list(map(int, input().split()))  # Read the array elements
    
    # Output the result
    print(minimum_swaps_to_beautiful(arr))
