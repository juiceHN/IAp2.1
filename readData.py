# Hugo Noriega
# 14097
import re
import random
from collections import Counter
from functools import reduce

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
    line = re.sub('[+.?!@#1234£&$567890:/;_=()-,<>\n]', '', line)
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

    return ham, spam, allHam, allSpam

# regresa uno de dos archivos: mensajes desordenados de ham o spam
# array = lista de mensajes
# mType = para confirmar si es ham o spam para el nombre


def shuffle_save(array, mType, arrayz=[]):
    array = array + arrayz
    random.shuffle(array)
    array2 = map(lambda x: x + '\n', array)
    if mType == 'spam':
        filename = 'allSpam.txt'
    if mType == 'ham':
        filename = 'allHam.txt'
    if mType == 'test':
        filename = 'pruebas.txt'
    with open(filename, 'w') as text:
        text.writelines(array2)
    print('done')

# funcion que prepara diccionarios con las palabras de los archivos
# regresa un diccionario y
# cantidad de lineas en el documento para control


def CreateDictionary(filename):
    dictionary = {}
    counter = 0
    size = file_len(filename)
    doc = open(filename, 'r')
    for i in range(size):
        temp = []
        line = doc.readline()
        line = cleanLine(line)
        temp = line.split('\t')
        mesage = temp[1]
        words = mesage.split(' ')
        counter += 1
        dictionary = saveWords(words, dictionary)

    return dictionary, counter


def createDictionary2(array):
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


# hamC, spamC, hamArray, spamArray = messageOrganizer('test_corpus.txt')
# print('hams: ', hamC, '\nspams: ', spamC)
# shuffle_save(hamArray, 'ham')
# shuffle_save(spamArray, 'spam')
# Dham, hcheck = CreateDictionary('ttt.txt')
# print(Dham, hcheck)
# Dspam, scheck = CreateDictionary('allSpam.txt')
# dataSeparator(hamC, hamArray)


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


def psh(messageC, allMessages, k):
    x = (messageC + k) / (allMessages + (k * 2))
    return x


def pword(wordFreq, k, shWord, allwords):
    x = (wordFreq + k) / (shWord + (k * allwords))
    return x


def pmessage(arrayS, arrayH, s, h, mType):
    pms = reduce(lambda x, y: x * y, arrayS)
    pmh = reduce(lambda x, y: x * y, arrayH)
    if mType == 'spam':
        numerator = pms * s
        denominator = numerator + (pmh * h)
        prob = numerator / denominator
    elif mType == 'ham':
        numerator = pmh * h
        denominator = numerator + (pms * s)
        prob = numerator / denominator

    return prob


def verifyMessage(line, dh, ds, mType, k, h, s):
    # todas las palabras en ham
    dhs = sum(dh.values())
    # todas las palabras enn spam
    dss = sum(ds.values())

    # nuevo diccionario
    d2 = addDictionaries(dhs, dss)
    # todas las palabras distintas
    d2s = len(d2)

    a, b, c, hamArray, spamArray = [], [], [], [], []
    a = line.split('\t')
    b.append(a[0])
    c = a[1].split(' ')
    for i in range(len(c)):
        pw = pword(dss[c[i]], k, dss, d2s)
        spamArray.append(pw)
        pw = pword(dhs[c[i]], k, dhs, d2s)
        hamArray.append(pw)

    probs = pmessage(spamArray, hamArray, s, h, mType)

    return probs

