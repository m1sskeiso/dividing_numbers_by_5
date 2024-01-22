# Exercise 6: Display numbers divisible by 5 from a list Iterate the given list of 
#numbers and print only those numbers which are divisible by 5

# Defining function for dividing numbers by divisible by 5
def displaying_numbers_divisible_by_five(input_list):
    # Iterate through the list
    for number in input_list:
        # Check if the number is divisible by 5
        if number % 5 == 0:
            print(number)

# Test case
numbers_list = [15, 25, 30, 35, 40, 45, 50, 55]
print("Numbers divisible by 5:")
displaying_numbers_divisible_by_five(numbers_list)
