#UPPERCASE = constant
#camelCase = var
#PascalCase = object
#lower_snake_case = file names
#imports - i don't think we need any for this one but if you do find somewhere that would be better to have one, go ahead and add one
#vars
c = 0
dummy = []
#key_file open
key_file = open("key_file.txt", "r")
#grabs key from key_file
key = key_file.readline(85)
#close key_file
key_file.close()

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

#this scrambles the message
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
 elif message[c] == KEYBASE[45]:
  message[c] = key[45]
 elif message[c] == KEYBASE[46]:
  message[c] = key[46]
 elif message[c] == KEYBASE[47]:
  message[c] = key[47]
 elif message[c] == KEYBASE[48]:
  message[c] = key[48]
 elif message[c] == KEYBASE[49]:
  message[c] = key[49]
 elif message[c] == KEYBASE[50]:
  message[c] = key[50]
 elif message[c] == KEYBASE[51]:
  message[c] = key[51]
 elif message[c] == KEYBASE[52]:
  message[c] = key[52]
 elif message[c] == KEYBASE[53]:
  message[c] = key[53]
 elif message[c] == KEYBASE[54]:
  message[c] = key[54]
 elif message[c] == KEYBASE[55]:
  message[c] = key[55]
 elif message[c] == KEYBASE[56]:
  message[c] = key[56]
 elif message[c] == KEYBASE[57]:
  message[c] = key[57]
 elif message[c] == KEYBASE[58]:
  message[c] = key[58]
 elif message[c] == KEYBASE[59]:
  message[c] = key[59]
 elif message[c] == KEYBASE[60]:
  message[c] = key[60]
 elif message[c] == KEYBASE[61]:
  message[c] = key[61]
 elif message[c] == KEYBASE[62]:
  message[c] = key[62]
 elif message[c] == KEYBASE[63]:
  message[c] = key[63]
 elif message[c] == KEYBASE[64]:
  message[c] = key[64]
 elif message[c] == KEYBASE[65]:
  message[c] = key[65]
 elif message[c] == KEYBASE[66]:
  message[c] = key[66]
 elif message[c] == KEYBASE[67]:
  message[c] = key[67]
 elif message[c] == KEYBASE[68]:
  message[c] = key[68]
 elif message[c] == KEYBASE[69]:
  message[c] = key[69]
 elif message[c] == KEYBASE[70]:
  message[c] = key[70]
 elif message[c] == KEYBASE[71]:
  message[c] = key[71]
 elif message[c] == KEYBASE[72]:
  message[c] = key[72]
 elif message[c] == KEYBASE[73]:
  message[c] = key[73]
 elif message[c] == KEYBASE[74]:
  message[c] = key[74]
 elif message[c] == KEYBASE[75]:
  message[c] = key[75]
 elif message[c] == KEYBASE[76]:
  message[c] = key[76]
 elif message[c] == KEYBASE[77]:
  message[c] = key[77]
 elif message[c] == KEYBASE[78]:
  message[c] = key[78]
 elif message[c] == KEYBASE[79]:
  message[c] = key[79]
 elif message[c] == KEYBASE[80]:
  message[c] = key[80]
 elif message[c] == KEYBASE[81]:
  message[c] = key[81]
 elif message[c] == KEYBASE[82]:
  message[c] = key[82]
 elif message[c] == KEYBASE[83]:
  message[c] = key[83]

 c += 1

dummy = ""
message = dummy.join(message)
print('message >>>' + message)