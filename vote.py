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

list1 = list1[:33]


def getListItem(a):
    thething = list1.index(a)
    return thething
def popItems(l):
    for x in l:
        list1.pop(getListItem(x))
    return
bsaver = []
def teir(*args):
    for n in reversed(args):
        b = list(n.strip())
        popItems(b)
        random.shuffle(b)
        bsaver.append(b)
    random.shuffle(list1)
    print("".join(x for x in list1), end='')
    for b in bsaver:
        print("".join(x for x in b), end='')
    print()
    
items = '''HA'''
teir("ZGC","", '')
#WORST FIRST

