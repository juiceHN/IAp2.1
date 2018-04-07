# Hugo Noriega
# 14097

from readData import *

# separar ham y spam
hamC, spamC, hamArray, spamArray = messageOrganizer('test_corpus.txt')
print('hams: ', hamC, '\nspams: ', spamC)

# guardar nuevos txt con ham y spam
shuffle_save(hamArray, 'ham')
shuffle_save(spamArray, 'spam')

# dividir data en distintos parametros
hTrainig, hCross, hTst = dataSeparator(hamC, hamArray)
sTraining, sCross, sTst = dataSeparator(spamC, spamArray)

messSpam = len(hTrainig)
messHam = len(sTraining)
totalMes = messSpam + messHam

# guarda txt para hacer tests
shuffle_save(hTst, 'test', sTst)

# creacion de diccionarios de palabras
hamD = createDictionary2(hTrainig)
spamD = createDictionary2(sTraining)

# tamano de los diccionarios
hamWords = len(hamD)
spamWords = len(spamD)

# todas las palabras en ham y spam
hamAllWords = sum(hamD.values())
spamAllWord = sum(spamD.values())

# todas las palabras distintas
allWords = addDictionaries(hamD, spamD)
numberOfWords = len(allWords)

k = 1

isSpam = psh(messSpam, totalMes, k)
isHam = psh(messHam, totalMes, k)


