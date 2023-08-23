def print_element_frequency(arr):
    frequency_dict = {}
    
    for element in arr:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1
    
    for element, frequency in frequency_dict.items():
        print(f"Element: {element}, Frequency: {frequency}")

# Example usage
elements = [3, 7, 6, 2, 10, 4, 6, 2, 10, 4]
print_element_frequency(elements)
