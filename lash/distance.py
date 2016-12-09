from __future__ import division
#from sketch import *
import math

def factorial(n): 
    if n < 2: return 1
    return reduce(lambda x, y: x*y, xrange(2, int(n)+1))

def prob(s, p, n):
    x = 1.0 - p

    a = n - s
    b = s + 1

    c = a + b - 1

    prob = 0.0

    for j in xrange(a, c + 1):
        prob += factorial(c) / (factorial(j)*factorial(c-j)) \
                * x**j * (1 - x)**(c-j)

    return prob


def hashLessThan(hash1, hash2):
    return hash1 < hash2


# def compare(input):
#     sketchRef = input.sketchRef
#     sketchQuery = input.sketchQuery

#     output = CompareOutput(input.sketchRef, input.sketchQuery, input.indexRef, input.indexQuery, input.pairCount)
#     if sketchQuery.getMinHashesPerWindow() < sketchRef.getMinHashesPerWindow():
#         sketchSize = sketchQuery.getMinHashesPerWindow()
#     else:
#         sketchSize = sketchRef.getMinHashesPerWindow()

#     i = input.indexQuery
#     j = input.indexRef

#     k = 0
#     while k < input.pairCount and i < sketchQuery.getReferenceCount()
#         compareSketches(output.pairs[k], sketchRef.getReference(j), sketchQuery.getReference(i), sketchSize, sketchRef.getKmerSize(), sketchRef.getKmerSpace(), input.maxDistance, input.maxPValue)
#         j += 1

#         if j ==  sketchRef.getReferenceCount():
#             j = 0
#             i += 1

#         k += 1

#     return output

#CompareOutput::Pairoutput output
# def compareSketches(output, refRef, refQry, sketchSize, kmerSize, kmerSpace, maxDistance, maxPValue):
def compareSketches(refRefName, refQryName):
    
    refRef = open(refRefName,'r')
    refQry = open(refQryName,'r')

    sketchCount1 = 0
    sketchCount2 = 0
    hashesSortedRef = []
    hashesSortedQry = []

    for ln in refRef:
        sketchCount1 += 1
        hashesSortedRef.append(ln.strip())

    for ln in refQry:
        sketchCount2 += 1
        hashesSortedQry.append(ln.strip())

    if sketchCount1 < sketchCount2:
        sketchSize = sketchCount1
    else:
        sketchSize = sketchCount2

    kmerSize = 21
    kmerSpace = 4 ** kmerSize

    i = 0
    j = 0
    common = 0
    denom = 0
    #hashlist
    # hashesSortedRef = refRef.hashesSorted
    # hashesSortedQry = refQry.hashesSorted
    

    # output.ifPass = False

    while denom < sketchSize and i < sketchCount1 and j < sketchCount2:
        # if hashLessThan(hashesSortedRef.at(i), hashesSortedQry.at(j), hashesSortedRef.get64()):
        if hashLessThan(hashesSortedRef[i], hashesSortedQry[j]):
            i += 1
        # elif hashLessThan(hashesSortedQry.at(j), hashesSortedRef.at(i), hashesSortedRef.get64()):
        elif hashLessThan(hashesSortedQry[j], hashesSortedRef[i]):
            j += 1
        else:
            i += 1
            j += 1
            common += 1

        denom += 1

    if denom < sketchSize:
        if i < sketchCount1:
            denom += sketchCount1 - i

        if j < sketchCount2:
            denom += sketchCount2 - j

        if denom > sketchSize:
            denom = sketchSize

    # print common
    # print denom
    distance = 0
    #notice the round up here!!
    jaccard = common / denom

    if common == denom:
        distance = 0
    elif common == 0:
        distance = 1
    else:
        # print jaccard
        #what does 1. here mean?
        distance = -math.log(2 * jaccard / (1 + jaccard), math.e) / kmerSize

    # if distance > maxDistance:
    #     return

    # output.numer = common
    # output.denom = denom
    # output.distance = distance
    # output.pValue = pValue(common, refRef.length, refQry.length,kmerSpace, denom)

    # if output.pValue > maxPValue:
    #     return

    # output.ifPass = True
    p = 0
    p = pValue(common, sketchCount1, sketchCount2, kmerSpace, denom)
    print 'distance:', distance
    print 'pValue:', p

def pValue(x, lengthRef, lengthQuery, kmerSpace, sketchSize):
    #x is the number of shared kmers between sketches of size s if genome1 and genome2
    if x == 0:
        return 1

    #r1 kmerSpace |sigama|k
    pX = 1 / (1 + kmerSpace / lengthRef)
    #r2
    pY = 1 / (1 + kmerSpace / lengthQuery)

    #j_r
    r = pX * pY / (pX + pY - pX * pY)
    # print pX
    # print pY
    # print x-1
    # print r
    # print sketchSize

    return prob(x-1, r, sketchSize)

def test():
    compareSketches('test.sig', 'test2.sig')


if __name__ == '__main__':
    test()