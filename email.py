#The program iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line.
email = input("Enter email address: ")
for ch in email:
    if ch == "@":
        break
    print(ch, end="")
