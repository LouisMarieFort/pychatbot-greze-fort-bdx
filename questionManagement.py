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

#tests
#cleanedQuestion = getCleanedQuestion("Qui a parlé en premier du climat ? officiellement grng zebi")
cleanedQuestion = getCleanedQuestion("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?")
intersection = getIntersectionWords(cleanedQuestion)
text = open("./cleaned/Nomination_Chirac1.txt", 'r', encoding = "UTF-8").read()
#print(getQuestionTf(text, intersection))
#print(getQuestionTfidfMatrix(intersection))
#print(intersection)
#print(getQuestionTf(intersection))
#print(getQuestionTfidfVector(getQuestionTf(intersection)))
#print(getDotProduct(getTfidfVectorOfDocument("Nomination_Chirac2.txt", createTfidfMatrix()), getQuestionTfidfVector(getQuestionTf(intersection))))
#print(getCosineSimilarity([7,2,5],[0,0,5]))
#print(getMostRelevantDocument(getQuestionTfidfVector(getQuestionTf(intersection))))
#print(getTfidfVectorOfDocument("Nomination_Sarkozy.txt"))
questionTf = getQuestionTf(intersection)
vector1 = getTfidfVectorOfDocument("Nomination.txt")
vector2 = getQuestionTfidfVector(questionTf)

print(getMostRelevantDocument(vector2))