#UPPERCASE = constant
#camelCase = var
#PascalCase = object
#lower_snake_case = file names
#imports
import random

#variables
DUMMY = ""
dKey = 0
key = 0
ans = 0
key_file = open('key_file.txt', 'w')
keyBase = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '0',
    '-',
    '=',
    '[',
    ']',
    ';',
    #the double backslash below this is because it gives an error with just one as you are cancelling the quotation mark
    '\\',
    '/',
    ',',
    '.',
    '/',
    '`',
    '~',
    '~',
    '_',
    '+',
    '{',
    '}',
    ':',
    '|',
    '<',
    '>',
    '?',
    ' '
]

#shuffling base
random.shuffle(keyBase)

#turning key into a string for easier input
key = (DUMMY.join(keyBase))

#input your own key
ans = input('do you have a key already?(y/n) >')
if ans == 'y':
 dKey = input('key >')
 if dKey.__len__() != keyBase.__len__():
  print('using generated key:inputted key has too many or too few characters')
 else:
     key = dKey

#add to file
key_file.write(key)
key_file.close()

print(key)