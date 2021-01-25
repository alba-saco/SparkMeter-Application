# prints every third element of list using recursion
def print_third_element_recursively(arr):
    if len(arr) >= 3:
        print(arr[2])
        arr = arr[3:]
        print_third_element_recursively(arr)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_third_element_recursively(array)
