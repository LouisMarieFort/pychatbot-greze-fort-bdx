from re import sub
from tfidfFunctions import *
from os import listdir
from math import sqrt

def getLoweredString(string : str) -> str:
    """Transforms any capital letter into a lower case one
        Argument :
            string : it has to be a string type of variable
        Return : 
            string.lower() : it returns a string
    """
    return string.lower()

def getStringWords(string : str) -> list:
    """Returns a list of all the words in a sentence
    Argument :
        string : takes in a string variable, a sentence
    Return :
        string.split() : it returns a list of all the words in the sentence
    """
    punctuation = {'\n', '!', ',', '?', ';'}
    specificPunctuation = {'-', "'", '.', ',\n'}
    for punctuationMark in specificPunctuation:
       string = string.replace(punctuationMark, ' ')    
    for punctuationMark in punctuation:
        string = string.replace(punctuationMark, '')
    string = sub(' +', ' ', string)
    return string.split()

def getCleanedQuestion(question : str) -> list:
    """Returns a list of all the words in a cleaned question
    Argument :
        question : takes in an uncleaned string variable (contains punctuation, has capital letters)
    Return :
        getStringWords(question) : it returns a list of all the words of the sentence, cleaned without punctuation
    """
    question = getLoweredString(question)
    return getStringWords(question)

def getIntersectionWords(wordsList : list, directory = "./cleaned/") -> list:
    """Creates and returns a list of the words present in both wordList and the documents
    Argument :
        wordsList : takes in a list of words to compare
        directory (optional) : the directory that contains the corpus of cleaned documents to compare to
    Return :
        intersection : returns a list of the intersections
    """
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
