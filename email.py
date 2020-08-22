Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #The program iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. 
email = input("Enter email address: ")
for ch in email:
    if ch == "@":
        break
    print(ch, end="")
