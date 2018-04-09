import re
import random
from collections import Counter

# funcion para conteo de lineas en un documento


def file_len(filename):
    with open(filename) as doc:
        for i, l in enumerate(doc):
            pass
    return i + 1

# funcion para la limpieza de una oracion
# quita los caracteres especiales y los numeros
# hace todas las letras minusculas


def cleanLine(line):
    char = "1234567890><&$€+-'_:/â=*@#%^+|£()-,;.?![]\n"
    for c in char:
        line = line.replace(c, "")
    line = line.lower()
    return line

# funcion que guarda los valores en diccionarios
# verifica que la palabra este en el diccionario
# si esta agrega 1 a su definicion
# si no esta lo agrega al diccionario y le asigna un 1 por default


def saveWords(array, dictionary):
    j = len(array)
    for i in range(j):
        if array[i] in dictionary:
            dictionary[array[i]] = dictionary[array[i]] + 1
        else:
            dictionary[array[i]] = 1
    return dictionary


# funcion que separa todo el corpus
# regresa dos arrays: mensajes desordenados de ham y spam
# regresa dos contadores de control


def messageOrganizer(filename):
    ham, spam = 0, 0
    allHam, allSpam = [], []
    lines = file_len(filename)
    doc = open(filename, 'r')
    for i in range(lines):
        temp = []
        line = doc.readline()
        line = cleanLine(line)
        temp = line.split('\t')
        if temp[0] == 'spam':
            spam += 1
            allSpam.append(line)

        else:
            ham += 1
            allHam.append(line)

    return allHam, allSpam


def createDictionary(array):
    dictionary = {}
    size = len(array)
    for i in range(size):
        temp = []
        line = array[i]
        line = cleanLine(line)
        temp = line.split('\t')
        message = temp[1]
        words = message.split(' ')
        dictionary = saveWords(words, dictionary)
    return dictionary


def shuffle_save(array, mType, shuf, arrayz=[]):
    rrrr = []
    if shuf == True:
        random.shuffle(array)

    array = array + arrayz
    array2 = map(lambda x: x + '\n', array)
    if mType == 'spam':
        filename = 'allSpam.txt'
    if mType == 'ham':
        filename = 'allHam.txt'
    if mType == 'test':
        filename = 'test.txt'
    with open(filename, 'w') as text:
        text.writelines(array2)


def dataSeparator(size, array):
    ta, cr, ts = [], [], []
    training = 80
    crossValiation = 10
    test = 10

    trainingNumber = round((size * training) / 100)
    crossNumber = round((size * crossValiation) / 100)
    testNumber = round((size * test) / 100)
    a = trainingNumber + crossNumber

    for i in range(size):
        if i < trainingNumber:
            ta.append(array[i])
        if i < a and i >= trainingNumber:
            cr.append(array[i])
        if i > a and i <= (a + testNumber):
            ts.append(array[i])

    return ta, cr, ts


def addDictionaries(d1, d2):
    a = [d1, d2]
    d3 = Counter()
    for i in a:
        d3.update(i)

    return d3
