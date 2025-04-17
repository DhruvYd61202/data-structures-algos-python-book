import random

# sorted_list = sorted(random.sample(range(20000), 10000))
sorted_list = []
# target = random.choice(sorted_list) # Randomly select a target from the sorted list
target = 250000
print(f"Searching for {target} in the sorted list...")

def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python List.
    The search only considers the portion from data[low] to data[high].
    """
    if low > high:
        return False, "Interval is empty"                 # Interval is empty; target not found
    else:
        mid = (low + high) // 2        # Find the midpoint of the interval
        if target == data[mid]:
            return True, mid
        elif target < data[mid]:
            #recur on the left portion
            return binary_search(data, target, low, mid - 1)
        else:
            #recur on the right portion
            return binary_search(data, target, mid + 1, high)
        

result, index = binary_search(sorted_list, target, 0, len(sorted_list) - 1)
if result:
    print(f"Found {target} at index {index}.")
else:
    print(f"{target} not found in the list.")