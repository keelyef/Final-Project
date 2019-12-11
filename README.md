My project is a password generator. It prompts the user to input the number of characters that he or she wants the password to contain. Then, it checks parameters based on the user's input, before generating the password. If the user responds to the question asking how many characters are desired in the password with anything that is not an integer, the program will tell the user that their response is invalid and to try again. Additionally, if the user inputs an integer that is less than seven, the program will not generate a password, but will prompt the user to enter a higher number of characters so that their password can be stronger. The password is generated within an external module that is imported at the start of the notebook. This module begins with a list of characters that could be included in the password (every letter of the alphabet, every number, and select special characters), then randomly selects them based on the user's input to create a password of that many characters. Therefore, the notebook flows as follows:

1) Asks the user their desired length of the password.
2) Validates whether or not their response is an integer.
  a) If the response is not an integer, prompts a different response.
3) Validates whether or not their response is greater than 8, so that a strong password may be generated.
  b) If the response is less than 8, prompts a different response.
  c) If the response is over 100, prompts a different response.
4) Generates a password based off of the number of characters the user enters.

The notebook should be run in order from top to bottom, as many functions within it build on each other and the last cell calls them properly to generate the password.}
