#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    """
    Calculate the sum of numbers within the specified range.
this is asking me to  add up numbers between two numbers. I will use addition with in the function to add.
    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).
this is saying to make sure that the arguments are intergers  
    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.
    accum = 0
    
    for i in range(start,end +1):
        accum += i
        print(accum)
    return(accum)

    # calculate_sum(start, end)
def find_smallest_number(start, end):
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
# i would use the min function but since it is asking to impelment logic to 
# find the smallest number within range I  will us a for loop.
    return min(start,end)
       
    # TODO: Return the found smalle
    

def find_largest_number(start, end):
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.
    biggest = 0 
    for largest_num in range(start,end +1):
        if largest_num > biggest:
            biggest = largest_num
    return biggest
# find_largest_number(start, end)
def count_even_numbers(start, end):
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.
    even_nums = []
    for x in range(start, end + 1):
        if x % 2 == 0:
           even_nums.append(x)
    return len(even_nums) 
# count_even_numbers(start, end)
def count_odd_numbers(start, end):
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.
    odd_nums = []
    for x in range(start, end +1):
        if x % 2 != 0:
           odd_nums.append(x)
    return len(odd_nums)
# count_odd_numbers(start, end)