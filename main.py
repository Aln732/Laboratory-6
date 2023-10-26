from encode import encode
from decode import decode

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
            if men_choice == '2':
                x = decode(password)
                print(x)
                break
            if men_choice == '3':
                exit()