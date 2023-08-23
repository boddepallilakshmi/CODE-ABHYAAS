def print_frequency_and_min(arr):
    frequency = {}
    min_item = float('inf')
    
    for item in arr:
        # Count the frequency of each element
        frequency[item] = frequency.get(item, 0) + 1
        
        # Update the minimum element
        if item < min_item:
            min_item = item
            
    print("Element\tFrequency")
    for item, freq in frequency.items():
        print(f"{item}\t{freq}")
        
    print(f"The minimum item is: {min_item}")

# Example array of elements
array = [5, 2, 8, 2, 3, 5, 8, 9, 1, 5]

# Call the function with the example array
print_frequency_and_min(array)
