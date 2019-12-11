{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf600
{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;\f1\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c100000;}
\margl1440\margr1440\vieww11160\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf0 \cb2 \expnd0\expndtw0\kerning0
My project is a password generator. It prompts the user to input the number of characters that he or she wants the password to contain. Then, it checks parameters based on the user's input, before generating the password. If the user responds to the question asking how many characters are desired in the password with anything that is not an integer, the program will tell the user that their response is invalid and to try again. Additionally, if the user inputs an integer that is less than seven, the program will not generate a password, but will prompt the user to enter a higher number of characters so that their password can be stronger. The password is generated within an external module that is imported at the start of the notebook. This module begins with a list of characters that could be included in the password (every letter of the alphabet, every number, and select special characters), then randomly selects them based on the user's input to create a password of that many characters. Therefore, the notebook flows as follows:\cb1 \
\cb2 1) Asks the user their desired length of the password.\cb1 \
\cb2 2) Validates whether or not their response is an integer.\cb1 \
\pard\pardeftab720\partightenfactor0

\f1 \cf0 \cb2 a) If the response is not an integer, prompts a different response.\
\pard\pardeftab720\partightenfactor0

\f0 \cf0 3) Validates whether or not their response is greater than 8, so that a strong password may be generated.\cb1 \
\pard\pardeftab720\partightenfactor0

\f1 \cf0 \cb2 b) If the response is less than 8, prompts a different response.\
c) If the response is over 100, prompts a different response.\
\pard\pardeftab720\partightenfactor0

\f0 \cf0 4) Generates a password based off of the number of characters the user enters.\cb1 \
\cb2 The notebook should be run in order from top to bottom, as many functions within it build on each other and the last cell calls them properly to generate the password.}