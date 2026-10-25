password = input("Enter a sample password: ")

has_upper = False
has_lower = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has_lower = True
    if ch.isdigit():
        has_digit = True

length_ok = len(password) >= 8

print("At least 8 characters:", length_ok)
print("Contains uppercase letter:", has_upper)
print("Contains lowercase letter:", has_lower)
print("Contains digit:", has_digit)

if length_ok and has_upper and has_lower and has_digit:
    print("Password policy: Valid")
else:
    print("Password policy: Invalid")
