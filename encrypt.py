#UPPERCASE = constant
#camelCase = var
#PascalCase = object
#lower_snake_case = file names
#imports - i don't think we need any for this one but if you do find somewhere that would be better to have one, go ahead and add one
#vars
dummy = []
key_file = open("key_file.txt", "r")
key = key_file.readline(85)
message = 0
encMessage = []
KEYBASE = [
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

message = input('enter message here >')

#turning key into an array for easier use
for i in key:
 dummy.append(i)
key = dummy

dummy = []

#doing the same for message
for i in message:
 dummy.append(i)
message = dummy

#it's 12:30 rn so ill continue this tomorrow, if you can see the pattern here go ahead and continue, only gotta do it 81 more times
for c in message:
 if message[c] == keyBase[0]:
  message[c] = key[0]
 elif message[c] == keyBase[1]:
  message[c] = key[1]
 elif message[c] == keyBase[2]:
  message[c] = key[2]
 elif message[c] == keyBase[3]:
  message[c] = key[3]