from re import sub
from tfidfFunctions import *


def getLoweredString(string : str) -> str:
    return string.lower()

def getStringWords(string : str) -> list:
    punctuation = {'\n', '!', ',', '?', ';'}
    specificPunctuation = {'-', "'", '.', ',\n'}
    for punctuationMark in specificPunctuation:
       string = string.replace(punctuationMark, ' ')    
    for punctuationMark in punctuation:
        string = string.replace(punctuationMark, '')
    string = sub(' +', ' ', string)
    return string.split()

def intersectionWords(wordsList : list, directory = "./cleaned/") -> list:
    corpusIdf = inverseDocumentFrequency(directory)
    intersection = list()
    for word in wordsList:
        if word in corpusIdf.keys():
            intersection.append(word)
    return intersection

#tests
print(intersectionWords(getStringWords(getLoweredString("Qui a parlé en premier du climat ? zebi"))))