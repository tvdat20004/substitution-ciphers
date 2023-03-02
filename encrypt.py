import random
ciphertext = input("Enter ciphertext:")

alphabet = list('abcdefghijklmnopqrstuvwxyz')
#create the key
# random.shuffle(shuffled := alphabet[:])
#for example:
shuffled = list('xyzabcdefghijklmnopqrstuvw')
dictionary = dict(zip(alphabet, shuffled))

encrypted = ''.join([
    dictionary[c]
    if c in dictionary else c
    for c in ciphertext
])
print(encrypted)