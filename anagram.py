# Input from the user
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

# Check if the sorted characters of both numbers are equal
if sorted(number1) == sorted(number2):
    print(f"{number1} and {number2} are anagrams.")
else:
    print(f"{number1} and {number2} are not anagrams.")
