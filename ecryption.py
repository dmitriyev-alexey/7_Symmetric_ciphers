from random import randint
from re import findall


def Coding(k, m):  
    return ''.join([chr((ord(x) + k) % 65536) for x in m])


def Decoding(k, m):  
    return ''.join([chr((ord(x) - k) % 65536) for x in m])


def nonkey(m):  
    max_char = 0
    key = 0
    for i in range(65536):
        tt = len(m.split(chr((32 + i) % 65536)))
        if tt > max_char:
            max_char = tt
            key = i
    return key


def Regular(text):
    template = r"[0-9]+"
    return findall(template, text)


def Vernam():
    text = "HELLO WORLD"

    crypt = ""
    keys = ""

    for c in text:
        key = randint(0, 25)
        keys += str(key) + " "
        if ord(c) < 65 or ord(c) > 90:
            crypt += " "
        else:
            gg = ord(c) + key - 13
            crypt += chr((gg % 26) + ord("A"))

    print(crypt)
    print(keys)

    arr = []
    key = ""
    for k in keys:
        if k != " ":
            key += k
        else:
            arr.append(key)
            key = ""
            continue

    decrypt = ""
    for k, c in enumerate(crypt):
        if ord(c) < 65 or ord(c) > 90:
            decrypt += " "
        else:
            gg = ord(c) - int(arr[k]) - 13
            decrypt += chr((gg % 26) + ord("A"))
    print(decrypt)


x = 5
a = Coding(x, 'Snap back to reality, ope there goes gravity')
print(a)
c = nonkey(a)
print(Decoding(x, a))
print(Decoding(c, a))
Vernam()
