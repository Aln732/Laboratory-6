from encode import encode


def main():
    print('''
Menu
-------------
1. Encode
2. Decode
3. Quit
   
    ''')


password = None

if __name__ == '__main__':
    while True:
        main()
        men_choice = input('Please enter an option: ')
        while True:
            if men_choice == '1':
                pass_to_encode = input('Password: ')
                password = encode(pass_to_encode)
                print(password)
                break
