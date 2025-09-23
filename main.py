list ={'a': '2', 'b': '3', 'c': '5', 'd': 'k', 'e': 'o', 'f': 'd', 'g': 'a', 'h': '9', 'i': '1', 'j': 'H', 'k': '4', 'l': 'O', 'm': 'T', 'n': '7',
          'o': '8', 'p': 'R', 'q': 'S', 'r': '6', 's': 'U', 't': 'V', 'u': 'W', 'v': 'X', 'w': 'Y', 'x': 'Z', 'y': '0', 'z': 'Q', 'A': 'p', 'B': '9', 'C': 'h',
            'D': 'n', 'E': '+', 'F': 'j', 'G': 'A', 'H': 'Y', 'I': 'v', 'J': 'S', 'K': '6', 'L': '11', 'M': 'c', 'N': 'P', 'O': 'aa', 'P': 'Q', 'Q': '97', 'R': '2', 'S': 'jk', 
            'T': 'k', 'U': 'B', 'V': '2c', 'W': '6g', 'X': 'p5', 'Y': '0', 'Z': 'Qq', '1': '!', '2': '@', '3': '#', '4': '$', '5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')',
              '!': '-', '@': '=', '#': '+', '$': '[', '%': ']', '^': '{', '&': '}', '*': ';', ':' : '5-', '(': ',', ')': '.', '-': '<', '=': '>', '+': '/', '[': '?', ']': '~', '{': '`', '}': ' '}

def hash(text):
    hashed = ''
    for char in text:
        if char in list:
            hashed += list[char]
        else:
            hashed += char
    return hashed

salt = 'as6'

def insert(text):
    mid = len(text) // 2
    return text[:mid] + salt + text[mid:]


def substitute(text):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    key=5
    for i in range(len(letters)):
        list[letters[i]] =letters[(i+key)%len(letters)]
    substituted = ''
    for char in text:
        if char in list:
            substituted += list[char]
        else:
            substituted += char
    return substituted

def fixed_hash(text):
    hashed = hash(text)
    salted = insert(hashed)
    total = 0
    for i in range(len(salted)):
        total += ord(salted[i]) * (i + 1)
    if len(text) < 16:
        hash_str = (text * 16) [:16]
    else:
        hash_str = text[:16]
    return hash_str

print(fixed_hash('labas'))
print(fixed_hash(hash(insert('labas'))))
print(fixed_hash(hash('labas')))
print(fixed_hash(insert('Labas')))
print(substitute(fixed_hash(hash(insert('labas'))))) 
print(substitute(fixed_hash(hash('labas'))))
print(substitute(fixed_hash(insert('Labas')))) 

print(hash('LabAs'))
print(hash('Labas'))
print(hash('labaS'))
print(hash('labas'))
print(hash('LABAS'))
print(hash('12345'))
print(insert('labas'))
print(hash(insert('labas')))
