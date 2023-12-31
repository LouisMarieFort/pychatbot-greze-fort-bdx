from math import log10
from os import listdir


def termFrequency(text: str) -> dict:
    """ Create a dictionary of the term frequency of each word
    Argument :
        text : the text of which we want the term frequency
               it has to be "clean" : in lowercase characters with no punctuation
    Return :
        dictionary : dictionary associating each word with its number of occurrences in the text
    """
    dictionary = dict()
    endIndex = len(text)
    while endIndex > 0:
        beginningIndex = endIndex
        while text[beginningIndex - 1] != ' ' and beginningIndex > 0:
            beginningIndex -= 1
        if text[beginningIndex : endIndex] not in dictionary.keys():
            dictionary[text[beginningIndex : endIndex]] = 1
        else:
            dictionary[text[beginningIndex : endIndex]] += 1
        endIndex = beginningIndex - 1
    return dictionary

def inverseDocumentFrequency(directory = "./cleaned/") -> dict:
    """ Create a dictionary of the inverse document frequency of each words in the texts
    Argument :
        directory (optional) : the directory that contains the corpus of cleaned documents
    Return :
        dictionary : dictionary associating each word with its IDF score
    """
    dictionary = dict()
    for fileName in listdir(directory):
        with open("./cleaned/" + fileName, 'r', encoding = "UTF-8") as currentFile:
            fileTermFrequency = termFrequency(currentFile.read())
            for word in fileTermFrequency:
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    for word in dictionary:
        dictionary[word] = log10(len(listdir(directory))/dictionary[word])
    return dictionary

def createTfidfMatrix(directory = "./cleaned/") -> list:
    """ Create a matrix of the TF-IDF of the corpus of documents
        Each row represents the TF_IDF of the word that is at index 0
        Then, each column corresponds to a different text
    Argument :
        directory (optional) : the directory that contains the corpus of cleaned documents
    Return :
        matrix : the TF-IDF matrix
    """
    matrix = []
    filesNamesList = listdir(directory)
    listOfTF = []                                                            #list of dictionaries
    for fileName in filesNamesList:
        with open(directory + fileName, 'r', encoding = "UTF-8") as file:
            listOfTF.append(termFrequency(file.read()))
    for wordAndIDF in inverseDocumentFrequency(directory).items():
        row = [wordAndIDF[0]]
        for column in range(len(filesNamesList)):
            if wordAndIDF[0] in listOfTF[column].keys():
                row.append(wordAndIDF[1] * listOfTF[column][wordAndIDF[0]])
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def getTfidfVectorOfDocument(fileName : str, directory = "./cleaned/") -> list:
    vector = list()
    tfidfMatrix = createTfidfMatrix(directory)
    fileIndex = 0
    isFound = None
    while fileIndex < len(listdir(directory)) and not isFound:
        if fileName == listdir(directory)[fileIndex]:
            isFound = True
        fileIndex += 1                        # On conserve la valeur supérieure puisque les indices de notre matrice TF-IDF sont de 1 de plus
    for row in tfidfMatrix:
        vector.append(row[fileIndex])
    return vector

def getQuestionTfidfVector(questionTf : dict, directory = "./cleaned/") -> list:
    vector = list()
    for wordAndIdf in inverseDocumentFrequency(directory).items():
        vector.append(questionTf[wordAndIdf[0]] * wordAndIdf[1])
    return vector

def getQuestionTf(intersection : list, directory = "./cleaned/") -> dict:
    dictionary = dict()
    corpusIdf = inverseDocumentFrequency(directory)
    for word in corpusIdf.keys():
        if word in intersection:
            dictionary[word] = intersection.count(word) / len(intersection)
        else:
            dictionary[word] = 0
    return dictionary