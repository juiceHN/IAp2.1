from readData import *
from functools import reduce
# P(spam)
# P(ham)


def psh(messageC, allMessages, k):
    x = (messageC + k) / (allMessages + (k * 2))
    return x

# P(word|ham)
# P(word|ham)


def pword(wordFreq, k, wordsInSH, allDifWords):
    x = (wordFreq + k) / (wordsInSH + (k * allDifWords))
    return x


def pMessage(message, dHam, dSpam, isHam, isSpam, k):
    ph, ps = [], []
    words = message.split(' ')
    diffWords = len(dHam) + len(dSpam)
    for i in words:
        if i in dHam:
            pw = pword(dHam[i], k, len(dHam), diffWords)
            ph.append(pw)
        else:
            pw = pword(0, k, len(dHam), diffWords)
            ph.append(pw)
        if i in dSpam:
            pw = pword(dSpam[i], k, len(dSpam), diffWords)
            ps.append(pw)
        else:
            pw = pword(0, k, len(dSpam), diffWords)
            ps.append(pw)

    prob = finalCalc(ph, ps, isHam, isSpam)
    return prob


def finalCalc(ph, ps, isHam, isSpam):
    pham = reduce(lambda x, y: x * y, ph)
    pspam = reduce(lambda x, y: x * y, ps)
    spam = (pspam * isSpam) / ((pspam * isSpam) + (pham * isHam))
    return spam


def analizeDoc(filename, dHam, dSpam, isHam, isSpam, k):
	s, h = 0, 0
	lines = file_len(filename)
	doc = open(filename, 'r')
	res = open('resultados.txt', 'w')
	for i in range(lines):
		line = doc.readline()
		line = cleanLine(line)
		probSpam = pMessage(line, dHam, dSpam, isHam, isSpam, k)
		if probSpam > 0.7:
			s += 1
			res.write('spam\t'+line+'\n')
		else:
			h += 1
			res.write('ham\t'+line+'\n')
	print('spam: ', str(s))
	print('ham: ',str(h))

