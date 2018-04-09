from probabilities import *


def opt(array, k, dHam, dSpam, isHam, isSpam):
    ans = []
    ours = []
    for i in array:
        line = i.split('\t')
        ans.append(line[0])
        ourA = pMessage(line[1], dHam, dSpam, isHam, isSpam, k)
        if ourA > 0.7:
            ours.append('spam')
        else:
            ours.append('ham')
    return ans, ours


def gradePerf(real, mine):
    ok = 0
    wrong = 0
    for i in range(len(real)):
        if real[i] == mine[i]:
            ok += 1
        else:
            wrong += 1
    grade = ok * 100 / len(real)
    print('ok', ok)
    print('wrong', wrong)
    return grade


def findK(ki, step, cont, array, dHam, dSpam, isHam, isSpam):
    start = 0
    while (start < cont):
        a, b = opt(array, ki, dHam, dSpam, isHam, isSpam)
        grade = gradePerf(a, b)
        print(grade)
        if grade > 95:
            start = cont + 1
        else:
            ki += step
    return ki
