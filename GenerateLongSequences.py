import random
import string

alphabet = "ARNDCQEGHILKMFPSTWYVBZX"

def generateSequence(alphabet, length):   
    return ''.join(random.choice(alphabet) for i in range(length))

def saveToFile(fileName, sequence):
    file = open(fileName, "w")
    file.write(sequence)
    file.close()

def format(string, index):
    length = len(string)
    result = ""
    interval = range(0, length, index)

    for i in range(len(interval)):
        result += string[interval[i-1]:interval[i]] + "\n"

    result += string[interval[-1]:] + "\n"

    return result

def createFastaFile(fileName, sequences, id, length, difference):
    file = open(fileName, "w")
    for i in range(sequences):
        title = f">{id}|{generateSequence(string.ascii_letters, 10)}|{i}"
        temp = generateSequence(alphabet, length - (random.randint(0, difference + 1) - 1))
        sequence = format(temp, 80)
        file.write(title + sequence + "\n")
    file.close()

createFastaFile("a.fasta", 10, "Test", 100, 5)
createFastaFile("a1.fasta", 10, "Test", 1000, 50)

#saveToFile("100.seq", generateSequence(100))
#saveToFile("1000.seq", generateSequence(1000))
#saveToFile("10000.seq", generateSequence(10000))
#saveToFile("100000.seq", generateSequence(100000))
#saveToFile("1000000.seq", generateSequence(1000000))