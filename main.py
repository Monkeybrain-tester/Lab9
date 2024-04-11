def encoder(password):
    result = ""
    for char in password:
        char = int(char)
        char += 3
        char = str(char)
        result += char
    return result

def decoder(password):
    result = ''
    for char in password:
        char = int(char)
        char -= 3
        char = str(char)
        result += char
    return result

while True:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    choice = input("Please enter an option:")

    try:
        choice = int(choice)

    except:
        print("thats not an int silly ;]")
    if choice == 1:
        passvvrd = input("Please enter your password to encode:")
        passvvrd = encoder(passvvrd)
        print("Your password has been encoded and stored!")

    elif choice == 2:
        print("The encoded password is ",passvvrd,", and the original password is ",decoder(passvvrd),".")

    elif choice == 3:
        exit()
    else:
        print("thats not 1-3")