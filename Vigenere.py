def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("".join(key))
   
def encryption(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("".join(cipher_text))

string = str(input("Plaintext: "))
string = string.upper()
keyword = str(input("Key: "))
keyword = keyword.upper()
key = generateKey(string, keyword)
cipher_text = encryption(string,key)
print("Ciphertext :", cipher_text)