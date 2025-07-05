from getpass_asterisk.getpass_asterisk import getpass_asterisk

def main():
    password = "letmein"

    while True:
        # getpass_asterisk will show the asterisk when user types the password
        guess = getpass_asterisk('Guess the password: ').strip().lower()
        if password == guess:
            print("Access granted!")
            break
        else:
            print("Access denied!")


if __name__ == '__main__':
    main()