def find_max_frequency(arr):
    frequency = {}
    
    # Count the frequency of each element in the array
    for item in arr:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    max_frequency = 0
    max_item = None
    
    # Find the maximum frequent item
    for item, freq in frequency.items():
        if freq > max_frequency:
            max_frequency = freq
            max_item = item
    
    print("Element\tFrequency")
    for item, freq in frequency.items():
        print(f"{item}\t{freq}")
    
    if max_item is not None:
        print(f"\nMaximum frequent item: {max_item} (Frequency: {max_frequency})")
    else:
        print("No items in the array.")

# Example usage
arr = [1, 2, 3, 2, 2, 3, 4, 5, 4, 4, 4]
find_max_frequency(arr)
