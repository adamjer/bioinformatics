import random
import string

def generateSequence(length):
    alphabet = string.ascii_uppercase
    print(alphabet)
    print(len(alphabet))
    return ''.join(random.choice(alphabet) for i in range(length))

def saveToFile(fileName, sequence):
    file = open(fileName, "w")
    file.write(sequence)
    file.close()

saveToFile("100.seq", generateSequence(100))
saveToFile("1000.seq", generateSequence(1000))
saveToFile("10000.seq", generateSequence(10000))
saveToFile("100000.seq", generateSequence(100000))
saveToFile("1000000.seq", generateSequence(1000000))