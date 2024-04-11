def encoder(password):
    result = ""
    for char in password:
        char = int(char)
        char += 3
        char = str(char)
        result += char
    return result

def dwcwdwr(password):
    result = ''
    for char in password:
        char = int(char)
        char -= 3
        char = str(char)
        result += char
    return result