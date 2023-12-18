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
    """ Creates and returns a list of the words present in both wordList and the documents
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
    """ Return the dot product of two vectors
    Arguments :
        vector1 : the list of coordinates representing the first vector
        vector2 : the list of coordinates representing the second vector
    Return :
        dotProduct : the dot product of the two vectors
    """
    dotProduct = 0
    for i in range(len(vector1)):
        dotProduct += vector1[i] * vector2[i]
    return dotProduct

def getVectorNorm(vector : list) -> float:
    """ Return the norm of a vector
    Argument :
        vector : the list of coordinates representing the vector
    Return :
        the norm of the vector using the square root of the sum of the coordinates
    """
    sum = 0
    for i in range(len(vector)):
        sum += vector[i] ** 2
    return sqrt(sum)

def getCosineSimilarity(vector1 : list, vector2 : list) -> float:
    """ Return the cosine similarity of two vectors
    Arguments :
        vector1 : the list of coordinates representing the first vector
        vector2 : the list of coordinates representing the second vector
    Return :
        the cosine similarity of the vectors using the dot product over the product of the norms
    """
    normProduct = (getVectorNorm(vector1) * getVectorNorm(vector2))
    if normProduct == 0:
        raise AssertionError("Calcul impossible pour cette question.\nVeuillez utiliser des mots plus proches du thème des textes.")
    else:
        return getDotProduct(vector1, vector2) / normProduct

def getMostRelevantDocument(questionVector : list, directory = "./cleaned/") -> str:
    """ Select the most relevant document
    Arguments :
        questionVector : the list of coordinates representing the question vector
    Return :
        the name of the most relevant document
    """
    cosineSimilarities = list()
    for fileName in listdir(directory):
        cosineSimilarities.append(getCosineSimilarity(getTfidfVectorOfDocument(fileName, directory), questionVector))
    return listdir(directory)[cosineSimilarities.index(max(cosineSimilarities))]

def getHighestTfidfOfQuestion(questionVector : list) -> str:
    """ return the word with the highest tfidf of the question
    Arguments :
        vector : the tfidf vector of the question
    Return :
        the word with the highest tfidf of the question
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

def getAnswerStarter(question: str) -> str:
    questionStarters = {"Comment": "Après analyse, ", 
                         "Pourquoi": "Car, ", 
                         "Peux-tu": "Oui, bien sûr, "}
    if question.split()[0] in questionStarters:
        return questionStarters[question.split()[0]]

        
def questionManagementToGetAnswer(question : str, directory = "./speeches/") -> None:
    """ Procedure for obtaining an answer to a question
    Argument : 
        question : the question we want to answer
        directory : the studied directory 
    Return :
        mostRelevantSentence : the answer to the question
    """
    answer = getAnswerStarter(question)
    mostRelevantSentence = None
    while mostRelevantSentence == None:                                          # Au cas où le mot avec le plus haut tfidf n'est pas dans le texte
        questionTfidfVector = getQuestionTfidfVector(getQuestionTf(getIntersectionWords(getCleanedQuestion(question))))
        highestTfidfOfQuestion = getHighestTfidfOfQuestion(questionTfidfVector)
        mostRelevantSentence = getMostRelevantSentence(highestTfidfOfQuestion, questionTfidfVector, directory)
        question = question.replace(highestTfidfOfQuestion, "")
    if answer == None:
        answer = mostRelevantSentence.lstrip()
    else:
        mostRelevantSentence = mostRelevantSentence.lstrip()
        answer += mostRelevantSentence.replace(mostRelevantSentence[0], mostRelevantSentence[0].lower())
    return answer