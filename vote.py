import sys
import io
sys.stdout = io.TextIOWrapper(buffer=sys.stdout.buffer,encoding='utf8')

import random
list1 = []
for i in range(65, 91):
    list1.append(chr(i))

for i in range(97, 123):
    list1.append(chr(i))
for i in range(10):
    list1.append(str(i))
list1.append("!")
for i in range(35, 43):
    if i != 39:
        list1.append(chr(i))
for i in range(44, 48):
    list1.append(chr(i))
for i in range(58, 65):
    if i != 61: 
        list1.append(chr(i)) 
for i in range(94, 97):
    list1.append(chr(i))
for i in range(123, 127):
    list1.append(chr(i))
for i in range(161, 163):
    list1.append(chr(i))
list1.append('£')
list1.append('¤')
list1.append('¥')
list1.append('¦')
list1.append('§')
list1.append('¨')
list1.append('ª')

#something here
try:
    list1 = list1[:int(sys.argv[1])]
    h = ""
except:
    h = str(sys.argv[1])


def getListItem(a):
    thething = list1.index(a)
    return thething
def popItems(l):
    for x in l:
        list1.pop(getListItem(x))
    return
bsaver = []
def teir(*args):
    result = ""
    for n in reversed(args):            # Reverse order of the teir function
        b = list(n.strip())             # I have no idea
        popItems(b)                     # Remove specific characters from our list
        random.shuffle(b)               # Shuffle our removed characters
        bsaver.append(b)                # Store our characters for later
    random.shuffle(list1)               # Shuffle our non-removed characters
    result += "".join(x for x in list1) # Append non-removed characters to result
    for b in bsaver:
        result += "".join(x for x in b) # Append removed characters to result
    return result

items = sys.argv[2:]

result = teir(h, *items)   # :)
#WORST FIRST

print(result)