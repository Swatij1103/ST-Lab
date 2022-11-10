charachter  = list(map(chr,range(ord('a'),ord('z')+1)))+list(map(chr,range(ord('A'),ord('Z')+1)))

def encode(text,key):
    cipher_text =""
    for x in text:
        if x == " ":
            cipher_text+="$"
        else:
            pos = charachter.index(x)
            cipher_text+=charachter[(pos+key)%52]
    return cipher_text

def decode(cipher,key):
    plain_text = ""
    for ciph in cipher:
        if ciph == "$":
            plain_text+=" "
        else:
            pos = charachter.index(ciph)
            plain_text+=charachter[(pos-key)%52]
    return plain_text

def calfrequency(text):
    frequency = dict()
    text_length = len(text)
    offset = 100/text_length
    for x in text:
        if x == "":
            continue
        elif x in frequency:
            frequency[x]+=offset
        else:
            frequency[x]=offset
    return frequency

plain_text = input("Enter the Text to encode : ")
key =int(input("Enter key : "))
cipher = encode(plain_text,key)
print(cipher)
text = decode(cipher,key)
print(text)
text = calfrequency(text)
print(text)

