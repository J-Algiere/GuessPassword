Requires getpass_asterisk to install use pip install getpass-asterisk

To import use from getpass_asterisk.getpass_asterisk import getpass_asterisk

If you dont want the asterisk for just use import getpass

Recommended to use the terminal or command prompt.

The getpass() or getpass_asterisk() function works perfectly in a system terminal or command prompt,
but in some IDEs (like VS Code's built-in terminal, IDLE, PyCharm, or web-based editors):
it may not display the prompt text, or It may fail entirely with an error like "GetPassWarning" or just no visible prompt.
This is due to how those environments handle secure input — they don’t fully support it.

It is important to note the security implications when choosing to display asterisk masks, as it reveals the length of the password.
For highly sensitive applications, the default behavior of getpass (no echo) is generally preferred.
