charachter  = list(map(chr,range(ord('a'),ord('z')+1)))+list(map(chr,range(ord('A'),ord('Z')+1)))

def calfrequency(plain_text):
    frequency = dict()
    text_length = len(plain_text)
    offset = 100/text_length
    for x in plain_text:
        if x == "":
            continue
        elif x in frequency:
            frequency[x]+=offset
        else:
            frequency[x]=offset
    return frequency

plain_text = input("Enter the Text to encode : ")
text = calfrequency(plain_text)
print(text)