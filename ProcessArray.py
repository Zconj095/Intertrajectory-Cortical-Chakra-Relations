import numpy as np
def process_array(arr):
    # Take the absolute value to avoid sqrt of negative numbers
    arr_abs = np.abs(arr)
    return np.sqrt(arr_abs) - np.cbrt(arr)

# Example usage
arr = np.array([1, -4, 9, -16])
result = process_array(arr)
print(result)