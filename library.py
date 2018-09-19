import des
from time import sleep
import sys 

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def splitIntoGroups(string,length):
    results = []
    loc = 0
    temp = ""
    while(loc < len(string)):
        temp += string[loc]
        loc += 1
        if loc % length == 0:
            results.append(temp)
            temp = ""
    return results

# from des import des 
 
def decrypt(message):
    toy = des.DES()

    entries = splitIntoGroups(message,8)
    decryptedMessages = []
    for i in range(len(entries)):
        decryption = toy.Decryption(entries[i])
        decryptedMessages.append(decryption)
    decryptedMessage ="".join(decryptedMessages)
    decryptedMessage = text_from_bits(decryptedMessage)
    return decryptedMessage

def encrypt(message):
    toy = des.DES()
    binary = text_to_bits(message)
    entries = splitIntoGroups(binary,8)
    # print(entries)

    encryptedEntries = []

    for i in range(len(entries)):
        encryptedMessage = toy.Encryption(entries[i])
        encryptedEntries.append(encryptedMessage)
    # print(encryptedEntries)


    finalEncryptedMessage = "".join(encryptedEntries)
    return finalEncryptedMessage

def sending():
    print("\nSending ",end = "")
    for j in range(5):
        sleep(0.4)
        print(".", end = "")
        sys.stdout.flush()
    print(' SENT')