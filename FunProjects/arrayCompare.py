'''Comparing arrays'''

'''This problem helps one to understand the key concepts of an array(list) in Python. 
Two arrays are said to be the same if they contain the same elements and in the same order.
However, in this problem, we will compare two arrays to see if they are same, but with a slight twist.
Here, two arrays are the same if the elements of one array are squares of elements of other arrays and regardless of the order. 
Consider two arrays a and b.

'''
# ''Comparing arrays'''

def comp(array1, array2):
    # Handle edge cases where one or both arrays could be None
    if array1 is None or array2 is None:
        return array1 == array2  # True only if both are None

    # Handle empty lists
    if array1 == [] and array2 == []:
        return True
    if array1 == [] or array2 == []:
        return False

    # Check if sorted squares of array1 equal sorted array2, or vice versa
    return sorted([i ** 2 for i in array1]) == sorted(array2) or \
           sorted([i ** 2 for i in array2]) == sorted(array1)

# Example usage:
result = comp([1, 2, 3, 4], [1, 4, 9, 16])
if result:
    print("The two arrays are same as the given condition")
else:
    print("The two arrays are not same as the given condition")

# User input
lis1 = eval(input("Enter list 1: "))
lis2 = eval(input("Enter list 2: "))
print(comp(lis1, lis2))

