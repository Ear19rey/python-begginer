import string

def encrypt(text, encryDict):
    cipher = []
    for i in text:
        cipher.append(encryDict[i])
    return ''.join(cipher)

abc=string.printable[:-3]
subText = abc[-3:] + abc[:-3]
encry_dict = dict(zip(subText, abc))
print(abc)

msg="Three members of the Australian athletics team remain in " \
    "isolation at the Tokyo Olympics after close contact with Ame" \
    "rican pole vaulter Sam Kendricks, who has tested positive for Covid-19."

ciphertext = encrypt(msg, encry_dict)
print(msg)
print(ciphertext)