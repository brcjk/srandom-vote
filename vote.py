import sys
import io
import random

sys.stdout = io.TextIOWrapper(buffer=sys.stdout.buffer,encoding='utf8')

list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', ',', '-', '.', '/', ':', ';', '<', '>', '?', '@', '^', '_', '`', '{', '|', '}', '~', '¡', '¢', '£', '¤', '¥', '¦', '§', '¨', 'ª']

#something here
try:
    list1 = list1[:None if sys.argv[1] == 'None' else int(sys.argv[1])]
except (ValueError, IndexError) as exc:
    raise TypeError("VAL must be a integer or None!") from exc


def get_list_item(a):
    thething = list1.index(a)
    return thething
def pop_items(l):
    for x in l:
        list1.pop(get_list_item(x))
bsaver = []
def teir(*args):
    result = ""
    for n in reversed(args):            # Reverse order of the teir function
        b = list(n.strip())             # I have no idea
        pop_items(b)                    # Remove specific characters from our list
        random.shuffle(b)               # Shuffle our removed characters
        bsaver.append(b)                # Store our characters for later
    random.shuffle(list1)               # Shuffle our non-removed characters
    result += "".join(x for x in list1) # Append non-removed characters to result
    for _b in bsaver:
        result += "".join(x for x in _b)# Append removed characters to result
    return result

items = sys.argv[2:]

RESULT = teir(*items)   # :)
# WORST FIRST

print(RESULT)
