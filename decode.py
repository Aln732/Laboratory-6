#Nicholas Silva
def decode(password):
    decoded = ''
    for i in password:
        if int(i)-3 == -3:
            decoded += '7'
        elif int(i)-3 == -2:
            decoded += '8'
        elif int(i)-3 == -1:
            decoded += '9'
        else:
            decoded += str(int(i)-3)
    return decoded


