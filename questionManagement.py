from re import sub
from tfidfFunctions import *
from os import listdir
from math import sqrt

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

def getDotProduct(vector1 : list, vector2 : list) -> float:
    dotProduct = 0
    for i in range(len(vector1)):
        dotProduct += vector1[i] * vector2[i]
    return dotProduct

def getVectorNorm(vector : list) -> float:
    sum = 0
    for i in range(len(vector)):
        sum += vector[i] ** 2
    return sqrt(sum)

def getCosineSimilarity(vector1 : list, vector2 : list) -> float:
    return getDotProduct(vector1, vector2) / (getVectorNorm(vector1) * getVectorNorm(vector2))

def getMostRelevantDocument(questionVector : list, directory = "./cleaned/") -> str:
    cosineSimilarities = list()
    for fileName in listdir(directory):
        cosineSimilarities.append(getCosineSimilarity(getTfidfVectorOfDocument(fileName, directory), questionVector))
    return listdir(directory)[cosineSimilarities.index(max(cosineSimilarities))]

def getHighestTfidfOfQuestion(questionVector : list) -> str:
    """
    temp : vector : le vecteur tfidf de la question
    """
    index = questionVector.index(max(questionVector))
    mots = list(inverseDocumentFrequency().keys())
    return mots[index]

def getMostRelevantSentence(word : str, vector : list, directory = "./speeches/") -> str :
    document = getMostRelevantDocument(vector)
    text = open(directory + document, "r", encoding = "UTF-8").read()
    sentences = text.split(".")
    for i in sentences:
        if word in i.lower():
            return i
        
def questionManagementToGetAnswer(question : str) -> None:
    """ Procedure for obtaining an answer to a question
    Argument : 
        question : the question we want to answer
    Return :
        mostRelevantSentence : the answer to the question
    """
    mostRelevantSentence = None
    while mostRelevantSentence == None:                                          # Au cas où le mot avec le plus haut tfidf n'est pas dans le texte
        questionTfidfVector = getQuestionTfidfVector(getQuestionTf(getIntersectionWords(getCleanedQuestion(question))))
        highestTfidfOfQuestion = getHighestTfidfOfQuestion(questionTfidfVector)
        mostRelevantSentence = getMostRelevantSentence(highestTfidfOfQuestion, questionTfidfVector)
        question = question.replace(highestTfidfOfQuestion, "")
    return mostRelevantSentence

#tests

print(questionManagementToGetAnswer("Comment une nation peut-elle prendre soin du impartial souveraineté supplémentaires ?"))