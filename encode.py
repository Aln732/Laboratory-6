def encode(string):
    encodedpassword = ''
    for i in string:
        c = (int(i) + 3) % 10
        encodedpassword += str(c)
    return encodedpassword

