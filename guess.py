from getpass_asterisk.getpass_asterisk import getpass_asterisk

"""
*** Recommended to use the terminal or command prompt. ***

The getpass() or getpass_asterisk() function works perfectly in a system terminal or command prompt,
but in some IDEs (like VS Code's built-in terminal, IDLE, PyCharm, or web-based editors):
it may not display the prompt text, or
It may fail entirely with an error like "GetPassWarning" or just no visible prompt.
This is due to how those environments handle secure input — they don’t fully support it.

"""

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