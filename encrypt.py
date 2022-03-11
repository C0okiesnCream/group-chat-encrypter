#UPPERCASE = constant
#camelCase = var
#PascalCase = object
#lower_snake_case = file names
#imports - i don't think we need any for this one but if you do find somewhere that would be better to have one, go ahead and add one
#vars
c = 0
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

#it's 1:00 rn so ill continue this tomorrow, if you can see the pattern here go ahead and continue, only gotta do it 40 more times
while c < len(message):
 if message[c] == KEYBASE[0]:
  message[c] = key[0]
 elif message[c] == KEYBASE[1]:
  message[c] = key[1]
 elif message[c] == KEYBASE[2]:
  message[c] = key[2]
 elif message[c] == KEYBASE[3]:
  message[c] = key[3]
 elif message[c] == KEYBASE[4]:
  message[c] = key[4]
 elif message[c] == KEYBASE[5]:
  message[c] = key[5]
 elif message[c] == KEYBASE[6]:
  message[c] = key[6]
 elif message[c] == KEYBASE[7]:
  message[c] = key[7]
 elif message[c] == KEYBASE[8]:
  message[c] = key[8]
 elif message[c] == KEYBASE[9]:
  message[c] = key[9]
 elif message[c] == KEYBASE[10]:
  message[c] = key[10]
 elif message[c] == KEYBASE[11]:
  message[c] = key[11]
 elif message[c] == KEYBASE[12]:
  message[c] = key[12]
 elif message[c] == KEYBASE[13]:
  message[c] = key[13]
 elif message[c] == KEYBASE[14]:
  message[c] = key[14]
 elif message[c] == KEYBASE[15]:
  message[c] = key[15]
 elif message[c] == KEYBASE[16]:
  message[c] = key[16]
 elif message[c] == KEYBASE[17]:
  message[c] = key[18]
 elif message[c] == KEYBASE[19]:
  message[c] = key[19]
 elif message[c] == KEYBASE[20]:
  message[c] = key[20]
 elif message[c] == KEYBASE[21]:
  message[c] = key[21]
 elif message[c] == KEYBASE[22]:
  message[c] = key[22]
 elif message[c] == KEYBASE[23]:
  message[c] = key[23]
 elif message[c] == KEYBASE[24]:
  message[c] = key[24]
 elif message[c] == KEYBASE[25]:
  message[c] = key[25]
 elif message[c] == KEYBASE[26]:
  message[c] = key[26]
 elif message[c] == KEYBASE[27]:
  message[c] = key[27]
 elif message[c] == KEYBASE[28]:
  message[c] = key[28]
 elif message[c] == KEYBASE[29]:
  message[c] = key[29]
 elif message[c] == KEYBASE[30]:
  message[c] = key[30]
 elif message[c] == KEYBASE[31]:
  message[c] = key[31]
 elif message[c] == KEYBASE[32]:
  message[c] = key[32]
 elif message[c] == KEYBASE[33]:
  message[c] = key[33]
 elif message[c] == KEYBASE[34]:
  message[c] = key[34]
 elif message[c] == KEYBASE[35]:
  message[c] = key[35]
 elif message[c] == KEYBASE[36]:
  message[c] = key[36]
 elif message[c] == KEYBASE[37]:
  message[c] = key[37]
 elif message[c] == KEYBASE[38]:
  message[c] = key[38]
 elif message[c] == KEYBASE[39]:
  message[c] = key[39]
 elif message[c] == KEYBASE[40]:
  message[c] = key[40]
 elif message[c] == KEYBASE[41]:
  message[c] = key[41]
 elif message[c] == KEYBASE[42]:
  message[c] = key[42]
 elif message[c] == KEYBASE[43]:
  message[c] = key[43]
 elif message[c] == KEYBASE[44]:
  message[c] = key[44]

 c += 1

dummy = " "
message = dummy.join(message)
print(message)