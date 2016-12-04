import sketch
import math
# sketchRefNew = 1
# sketchQueryNew = 2
# indexRefNew = 3
# indexQueryNew = 4
# pairCountNew = 5
# parametersNew = 6
# maxDistanceNew = 7
# maxPValueNew = 8

class CompareInput:

    def __init__(self, sketchRefNew, sketchQueryNew, indexRefNew, indexQueryNew, pairCountNew, parametersNew, maxDistanceNew, maxPValueNew):
        # self.__dict__.update(data)
        self.sketchRef = sketchRefNew
        self.sketchQuery = sketchQueryNew
        self.indexRef = indexRefNew
        self.indexQuery = indexQueryNew
        self.pairCount = pairCountNew
        self.parameters = parametersNew
        self.maxDistance = maxDistanceNew
        self.maxPValue = maxPValueNew




# i = CompareInput(sketchRefNew, sketchQueryNew, indexRefNew,
#     indexQueryNew, pairCountNew, parametersNew, maxDistanceNew, maxPValueNew)
# print(i.sketchRef)


# a = 1
# b = 2
# c = 3
# d = 4
# e = 5

class PairOutput:
        def __init__(self, pairCountNew):
            pass
            # numer
            # denom
            # distance
            # pValue
            # ifPass


class CompareOutput:

    def __init__(self, sketchRefNew, sketchQueryNew, indexRefNew, indexQueryNew, pairCountNew):
        self.sketchRef = sketchRefNew
        self.sketchQuery = sketchQueryNew
        self.indexRef = indexRefNew
        self.indexQuery = indexQueryNew
        self.pairCount = pairCountNew
        self.pairs = PairOutput(pairCountNew)

    

# j = CompareOutput(a,b,c,d,e)
# print(j.sketchRef)


def CommandDistance():
    pass


def run():
    pass

#CompareOutput *output bool table
def __writeOutput(output, table):
    i = output.indexQuery
    j = output.indexRef
    k = 0
    while k < output.pairCount and i < output.sketchQuery.getReferenceCount():
        pair = output.pairs[k]
        if table and j == False:
            print(output.sketchQuery.getReference(i).name)
        
        if table == True:
            print('\t')
            if (pair.ifPass == True):
                print(pair.distance)
        elif pair.ifPass == True:
            print(output.sketchRef.getReference(j).name + "\t" + output.sketchQuery.getReference(i).name + "\t" + pair.distance + "\t" + pair.pValue + "\t" + pair.numer + "\t" + pair.denom, end="")

        j += 1

        if j == output.sketchRef.getReferenceCount():
            if table == True:
                print()

            j = 0
            i += 1
        
        k += 1

#CompareInput input
def compare(input):
    sketchRef = input.sketchRef
    sketchQuery = input.sketchQuery

    output = CompareOutput(input.sketchRef, input.sketchQuery, input.indexRef, input.indexQuery, input.pairCount)
    if sketchQuery.getMinHashesPerWindow() < sketchRef.getMinHashesPerWindow():
        sketchSize = sketchQuery.getMinHashesPerWindow()
    else:
        sketchSize = sketchRef.getMinHashesPerWindow()

    i = input.indexQuery
    j = input.indexRef

    k = 0
    while k < input.pairCount and i < sketchQuery.getReferenceCount()
        compareSketches(output.pairs[k], sketchRef.getReference(j), sketchQuery.getReference(i), sketchSize, sketchRef.getKmerSize(), sketchRef.getKmerSpace(), input.maxDistance, input.maxPValue)
        j += 1

        if j ==  sketchRef.getReferenceCount():
            j = 0
            i += 1

        k += 1

    return output

#CompareOutput::Pairoutput output
def compareSketches(output, refRef, refQry, sketchSize, kmerSize, kmerSpace, maxDistance, maxPValue):
    i = 0
    j = 0
    common = 0
    denom = 0
    #hashlist
    hashesSortedRef = refRef.hashesSorted
    hashesSortedQry = refQry.hashesSorted

    output.ifPass = False

    while denom < sketchSize and i < hashesSortedRef.size() and j < hashesSortedQry.size():
        if hashLessThan(hashesSortedRef.at(i), hashesSortedQry.at(j), hashesSortedRef.get64()):
            i += 1
        elif hashLessThan(hashesSortedQry.at(j), hashesSortedRef.at(i), hashesSortedRef.get64()):
            j += 1
        else:
            i += 1
            j += 1
            common += 1

        denom += 1

    if denom < sketchSize:
        if i < hashesSortedRef.size():
            denom += hashesSortedRef.size() - i

        if j < hashesSortedQry.size():
            denom += hashesSortedQry.size() - j

        if denom > sketchSize:
            denom = sketchSize

    distance
    #notice the round up here!!
    jaccard = common / denom

    if common == denom:
        distance = 0
    elif common == 0:
        distance = 1
    else:
        #what does 1. here mean??
        distance = -math.log(2 * jaccard / (1. + jaccard)) /kmerSize

    if distance > maxDistance:
        return


    output.numer = common
    output.denom = denom
    output.distance = distance
    output.pValue(common, refRef.length, refQry.length,kmerSpace, denom)

    if output.pValue > maxPValue:
        return

    output.ifPass = True



def pValue(x, lengthRef, lengthQuery, kmerSpace, sketchSize):
    #what does 1. here mean
    if x == 0:
        return 1.

    pX = 1. / (1. + kmerSpace / lengthRef)
    pY = 1. / (1. + kmerSpace / lengthQuery)

    r = pX * pY / (pX + pY - pX * pY)
    # M = kmerSpace * (pX + pY) / (1. + r);
    # return gsl_cdf_hypergeometric_Q(x - 1, r * M, M - r * M, sketchSize);

    