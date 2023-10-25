def encode(string):
    encodedpassword = ''
    for i in string:
        c = (int(i) + 3) % 10
        encodedpassword += str(c)
    return encodedpassword


def main():
    print('''
Menu
-------------
1. Encode
2. Decode
3. Quit
   
    ''')


if __name__ == '__main.py__':
    main()
    men_choice = input('Please enter an option: ')
    while True:
        if men_choice == '1':
            pass_to_encode = input('Password: ')
            print(encode(pass_to_encode))
