#UPPERCASE = constant
#camelCase = var
#PascalCase = object
#lower_snake_case = file names
#imports - i don't think we need any for this one either but if you do find somewhere that would be better to have one, go ahead and add one
#vars
c = 0
dummy = []
#key_file open
key_file = open("key_file.txt", "r")
#grabs key from key_file
key = key_file.readline(85)
#close key_file
key_file.close()

message = input('encrypted message here >')
deMessage = 0
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

#turning key into an array for easier use
for i in key:
 dummy.append(i)
key = dummy

dummy = []

#doing the same for message
for i in message:
 dummy.append(i)
message = dummy

#this unscrambles the message
while c < len(message):
 if message[c] == key[0]:
  message[c] = KEYBASE[0]
 elif message[c] == key[1]:
  message[c] = KEYBASE[1]
 elif message[c] == key[2]:
  message[c] = KEYBASE[2]
 elif message[c] == key[3]:
  message[c] = KEYBASE[3]
 elif message[c] == key[4]:
  message[c] = KEYBASE[4]
 elif message[c] == key[5]:
  message[c] = KEYBASE[5]
 elif message[c] == key[6]:
  message[c] = KEYBASE[6]
 elif message[c] == key[7]:
  message[c] = KEYBASE[7]
 elif message[c] == key[8]:
  message[c] = KEYBASE[8]
 elif message[c] == key[9]:
  message[c] = KEYBASE[9]
 elif message[c] == key[10]:
  message[c] = KEYBASE[10]
 elif message[c] == key[11]:
  message[c] = KEYBASE[11]
 elif message[c] == key[12]:
  message[c] = KEYBASE[12]
 elif message[c] == key[13]:
  message[c] = KEYBASE[13]
 elif message[c] == key[14]:
  message[c] = KEYBASE[14]
 elif message[c] == key[15]:
  message[c] = KEYBASE[15]
 elif message[c] == key[16]:
  message[c] = KEYBASE[16]
 elif message[c] == key[17]:
  message[c] = KEYBASE[18]
 elif message[c] == key[19]:
  message[c] = KEYBASE[19]
 elif message[c] == key[20]:
  message[c] = KEYBASE[20]
 elif message[c] == key[21]:
  message[c] = KEYBASE[21]
 elif message[c] == key[22]:
  message[c] = KEYBASE[22]
 elif message[c] == key[23]:
  message[c] = KEYBASE[23]
 elif message[c] == key[24]:
  message[c] = KEYBASE[24]
 elif message[c] == key[25]:
  message[c] = KEYBASE[25]
 elif message[c] == key[26]:
  message[c] = KEYBASE[26]
 elif message[c] == key[27]:
  message[c] = KEYBASE[27]
 elif message[c] == key[28]:
  message[c] = KEYBASE[28]
 elif message[c] == key[29]:
  message[c] = KEYBASE[29]
 elif message[c] == key[30]:
  message[c] = KEYBASE[30]
 elif message[c] == key[31]:
  message[c] = KEYBASE[31]
 elif message[c] == key[32]:
  message[c] = KEYBASE[32]
 elif message[c] == key[33]:
  message[c] = KEYBASE[33]
 elif message[c] == key[34]:
  message[c] = KEYBASE[34]
 elif message[c] == key[35]:
  message[c] = KEYBASE[35]
 elif message[c] == key[36]:
  message[c] = KEYBASE[36]
 elif message[c] == key[37]:
  message[c] = KEYBASE[37]
 elif message[c] == key[38]:
  message[c] = KEYBASE[38]
 elif message[c] == key[39]:
  message[c] = KEYBASE[39]
 elif message[c] == key[40]:
  message[c] = KEYBASE[40]
 elif message[c] == key[41]:
  message[c] = KEYBASE[41]
 elif message[c] == key[42]:
  message[c] = KEYBASE[42]
 elif message[c] == key[43]:
  message[c] = KEYBASE[43]
 elif message[c] == key[44]:
  message[c] = KEYBASE[44]
 elif message[c] == key[45]:
  message[c] = KEYBASE[45]
 elif message[c] == key[46]:
  message[c] = KEYBASE[46]
 elif message[c] == key[47]:
  message[c] = KEYBASE[47]
 elif message[c] == key[48]:
  message[c] = KEYBASE[48]
 elif message[c] == key[49]:
  message[c] = KEYBASE[49]
 elif message[c] == key[50]:
  message[c] = KEYBASE[50]
 elif message[c] == key[51]:
  message[c] = KEYBASE[51]
 elif message[c] == key[52]:
  message[c] = KEYBASE[52]
 elif message[c] == key[53]:
  message[c] = KEYBASE[53]
 elif message[c] == key[54]:
  message[c] = KEYBASE[54]
 elif message[c] == key[55]:
  message[c] = KEYBASE[55]
 elif message[c] == key[56]:
  message[c] = KEYBASE[56]
 elif message[c] == key[57]:
  message[c] = KEYBASE[57]
 elif message[c] == key[58]:
  message[c] = KEYBASE[58]
 elif message[c] == key[59]:
  message[c] = KEYBASE[59]
 elif message[c] == key[60]:
  message[c] = KEYBASE[60]
 elif message[c] == key[61]:
  message[c] = KEYBASE[61]
 elif message[c] == key[62]:
  message[c] = KEYBASE[62]
 elif message[c] == key[63]:
  message[c] = KEYBASE[63]
 elif message[c] == key[64]:
  message[c] = KEYBASE[64]
 elif message[c] == key[65]:
  message[c] = KEYBASE[65]
 elif message[c] == key[66]:
  message[c] = KEYBASE[66]
 elif message[c] == key[67]:
  message[c] = KEYBASE[67]
 elif message[c] == key[68]:
  message[c] = KEYBASE[68]
 elif message[c] == key[69]:
  message[c] = KEYBASE[69]
 elif message[c] == key[70]:
  message[c] = KEYBASE[70]
 elif message[c] == key[71]:
  message[c] = KEYBASE[71]
 elif message[c] == key[72]:
  message[c] = KEYBASE[72]
 elif message[c] == key[73]:
  message[c] = KEYBASE[73]
 elif message[c] == key[74]:
  message[c] = KEYBASE[74]
 elif message[c] == key[75]:
  message[c] = KEYBASE[75]
 elif message[c] == key[76]:
  message[c] = KEYBASE[76]
 elif message[c] == key[77]:
  message[c] = KEYBASE[77]
 elif message[c] == key[78]:
  message[c] = KEYBASE[78]
 elif message[c] == key[79]:
  message[c] = KEYBASE[79]
 elif message[c] == key[80]:
  message[c] = KEYBASE[80]
 elif message[c] == key[81]:
  message[c] = KEYBASE[81]
 elif message[c] == key[82]:
  message[c] = KEYBASE[82]
 elif message[c] == key[83]:
  message[c] = KEYBASE[83]

 c += 1

dummy = ""
message = dummy.join(message)
print('message >>>',message)