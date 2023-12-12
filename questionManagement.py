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

def getCleanedQuestion(question : str) -> list:
    question = getLoweredString(question)
    return getStringWords(question)

def getIntersectionWords(wordsList : list, directory = "./cleaned/") -> list:
    corpusIdf = inverseDocumentFrequency(directory)
    intersection = list()
    for word in wordsList:
        if word in corpusIdf.keys():
            intersection.append(word)
    return intersection

def getQuestionTf(text : str, intersection : list) -> dict:
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
            dictionary[text[beginningIndex : endIndex]] = 0
        endIndex = beginningIndex - 1
    for word in intersection:
        if word in dictionary.keys():
            dictionary[word] += 1
    return dictionary

def getQuestionTfidfMatrix(intersection : list, directory = "./cleaned/") -> list:
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
            listOfTF.append(getQuestionTf(file.read(), intersection))
    for wordAndIDF in inverseDocumentFrequency(directory).items():
        row = [wordAndIDF[0]]
        for column in range(len(filesNamesList)):
            if wordAndIDF[0] in listOfTF[column].keys():
                row.append(wordAndIDF[1] * listOfTF[column][wordAndIDF[0]])
            else:
                row.append(0)
        matrix.append(row)
    return matrix

#tests
cleanedQuestion = getCleanedQuestion("Qui a parlé en premier du climat ? officiellement zebi")
intersection = getIntersectionWords(cleanedQuestion)
text = open("./cleaned/Nomination_Chirac1.txt", 'r', encoding = "UTF-8").read()
#print(getQuestionTf(text, intersection))
print(getQuestionTfidfMatrix(intersection))