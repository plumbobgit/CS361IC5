def is_palindrome(a):
    return a == a[::-1]


a = input("Enter a string: ")

if is_palindrome(a):
    print("Yes")
else:
    print("No")
