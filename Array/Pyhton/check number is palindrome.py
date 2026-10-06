# Function to check if a number is a palindrome
def isPalindrome(num):
    # Store the original number
    original = num
    # Variable to store the reversed number
    reversed = 0

    # Reverse the number.
    while num > 0:
        # Get the last digit
        digit = num % 10
        # Build the reversed number
        reversed = reversed * 10 + digit
        # Remove the last digit
        num //= 10

    # Check if the original number is equal to the reversed number
    return original == reversed


arr = [111, 121, 134]

for num in arr:
    if isPalindrome(num):
        print(num, "is a palindrome.")
    else:
        print(num, "is not a palindrome.")

# Output:
# 111 is a palindrome.
# 121 is a palindrome.
# 134 is not a palindrome.


'''
TIME: O(d) per number, where d is its number of digits.
Each iteration removes one digit.
For n numbers with at most d digits each, total time is O(n * d).

EXTRA SPACE: O(1) under the usual constant-time integer arithmetic model.
Only a fixed number of variables are used.
'''
