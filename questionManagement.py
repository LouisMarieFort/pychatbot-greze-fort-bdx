from re import sub
from tfidfFunctions import *


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

def highestTfidfOfQuestion(vector : list) -> str:
    """
    temp : vector : le vecteur tfidf de la question
    """
    index = questionTfidfVector.index(max(questionTfidfVector))
    mots = list(inverseDocumentFrequency().keys())
    return mots[index]

def MostRelevantSentence(word,vector : list,directory = "./speeches/") -> str :
    document = getMostRelevantDocument(vector)
    text = open(directory+document,"r",encoding = "UTF-8").read()
    sentences = document.split(".")
    for i in sentences :
        if word in i :
            return i

#tests
cleanedQuestion = getCleanedQuestion("Qui a parlé en premier du climat ? officiellement zebi")
intersection = getIntersectionWords(cleanedQuestion)
text = open("./cleaned/Nomination_Chirac1.txt", 'r', encoding = "UTF-8").read()
#print(getQuestionTf(text, intersection))
print(getQuestionTfidfMatrix(intersection))
