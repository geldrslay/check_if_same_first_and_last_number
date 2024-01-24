# Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Defining function 

def check_if_same_first_and_last(number_list):
    # Display the given list
    print ('The given list is:', number_list)
    # Get the first and last number from the given list
    first_number = number_list[0]
    last_number = number_list [-1]
    # Check if the first and last number is the same and return result
    if first_number == last_number: 
        return True
    else: return False

# First given number list
first_number_list = [10,20,30,40,10]
print ('Is the first and last number the same?:', check_if_same_first_and_last(first_number_list))

# Second given number list
second_number_list = [75, 65, 35, 75, 30]
print ('Is the first and last number the same?:', check_if_same_first_and_last(second_number_list))

# Additional example 
third_number_list = [11,32,45,76,90,11]
print ('Is the first and last number the same?:', check_if_same_first_and_last(third_number_list))