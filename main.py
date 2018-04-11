from readData import *
from probabilities import *
from bestK import *
import random

hamArray, spamArray = messageOrganizer('test_corpus.txt')
shuffle_save(hamArray, 'ham', True)
shuffle_save(spamArray, 'spam', True)

th, ch, tsh = dataSeparator(len(hamArray), hamArray)
ts, cs, tss = dataSeparator(len(spamArray), spamArray)
csh = ch + cs
shuffle_save(tsh, 'test', False, tss)
dspam = createDictionary(ts)
dham = createDictionary(th)
allTm = len(th) + len(ts)
k = 1
isSpam = psh(len(ts), allTm, k)
isHam = psh(len(th), allTm, k)
newk = findK(k, 0.1, 1000, csh, dham, dspam, isHam, isSpam)
filename = 'test_sms.txt'
analizeDoc(filename, dham, dspam, isHam, isSpam, newk)
