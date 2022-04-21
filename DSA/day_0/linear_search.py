#Algorithm to find a number in the list of 10 numbers

#list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#num_to_find = int(input("Enter a number to find in the list of 10 numbers :: "))


#i = 0


#for i in range(len(list_of_numbers)):
#    if num_to_find == list_of_numbers[i]:
#        print("The number's position is :: ", i)
#   The upper part was my demo code


def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns -1
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return -1

def verify(index):
    if index != -1:
        print('Target found at index', index)
    else:
        print('Target not found in the list')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result= linear_search(numbers, 3)

verify(result)
