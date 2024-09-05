def is_palindrome(s):
    # Convert the string to lowercase and remove spaces
    s = s.lower().replace(" ", "")
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Input from the user
user_input = input("Enter a word or phrase: ")

# Check if the input is a palindrome
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
