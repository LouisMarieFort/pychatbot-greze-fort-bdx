from dataPreprocessingFunctions import *
from authorManagementFunctions import *
from tfidfFunctions import *
from os import listdir

def createUselessWordsList(directory = "./cleaned/") -> list:
    """ Create a list that contains all the words whose TF-IDF score is zero for each text
    Argument :
        directory (optional) : the directory that contains the corpus of cleaned documents
    Return :
        uselessWords : the list of all the useless words
    """
    tfidfMatrix = createTfidfMatrix(directory)
    uselessWords = []
    numberOfTexts = len(tfidfMatrix[0])
    for row in range(len(tfidfMatrix)):
        isUseless = True
        column = 1
        while column < numberOfTexts and isUseless:
            if tfidfMatrix[row][column] != 0:
                isUseless = False
            column += 1
        if isUseless:
            uselessWords.append(tfidfMatrix[row][0])
    return uselessWords

def mostRepeatedWords(authorsName = "Chirac", directory = "./cleaned/") -> list:
    """ Create a list of the words an author has repeated the most
    Argument :
        authorsName : the name of the author to study
    Return :
        repeatedWords : the list containing the most repeated words
    """
    filesList = []
    totalText = ""
    for file in listdir(directory):
        if findAuthorsName(file) == authorsName:
            filesList.append(file)
    for fileName in filesList:
        with open(directory + fileName, 'r', encoding = "UTF-8") as currentFile:
            totalText += ' ' + currentFile.read()
    for word in createUselessWordsList(directory):
        totalText = totalText.replace(word + ' ', '')
    totalTf = termFrequency(totalText)
    maximalOccurenceNumber = max(totalTf.values())
    repeatedWords = []
    for word in totalTf:
        if totalTf[word] == maximalOccurenceNumber :
            repeatedWords.append(word)
    return repeatedWords

def createHigherTfidfWordsList(directory = "./cleaned/") ->  list:
    """ Create the list of the words that have the higher TF-IDF score
    Argument :
        directory (optional) : the directory that contains the corpus of cleaned documents
    Return :
        wordsList : the list of the words that have the higher TF-IDF score
    """
    tfidfMatrix = createTfidfMatrix(directory)
    higherTfidf = 0
    wordsList = []
    for row in range(len(tfidfMatrix)):
        if max(tfidfMatrix[row][1:]) > higherTfidf:
            higherTfidf = max(tfidfMatrix[row][1:])
            wordsList = [tfidfMatrix[row][0]]
        elif max(tfidfMatrix[row][1:]) == higherTfidf:
            wordsList.append(tfidfMatrix[row][0])
    return wordsList

def findAuthorsWhoMentioned(word: str, directory = "./cleaned/") -> list:
    """ Create a list of the authors who said a specific word
    Argument :
        word : the word that we want to study
    Return :
        authorsWhoMentioned : the list of the authors' last names
    """
    word = word.lower() 
    authorsWhoMentioned = dict()
    for fileName in listdir(directory):
        nameOfTheAuthor = findAuthorsName(fileName)
        currentFile = open(directory + fileName, 'r', encoding = "UTF-8")
        currentTF = termFrequency(currentFile.read())
        currentFile.close()
        if word in currentTF.keys():
            if nameOfTheAuthor not in authorsWhoMentioned.keys():
                authorsWhoMentioned[nameOfTheAuthor] = currentTF[word]
            else:
                authorsWhoMentioned[nameOfTheAuthor] += currentTF[word]
    return authorsWhoMentioned

def findAuthorsWhoMostRepeated(word: str, directory = "./cleaned/") -> list:
    """ Create a list of the authors who have said a specific word the most
    Argument :
        word : the word that we want to study
    Return :
        authorsWhoMentioned : the list of the authors' last names
    """
    word = word.lower()
    authorsWhoMentioned = findAuthorsWhoMentioned(word, directory)
    maximalOccurences = max(authorsWhoMentioned.values())
    authorsWhoMostRepeated = []
    for author in authorsWhoMentioned.keys():
        if authorsWhoMentioned[author] == maximalOccurences:
            authorsWhoMostRepeated.append(author)
    return authorsWhoMostRepeated

def findFirstToMention(word : str) -> str:
    """ Find the first author (president) who said a specific word
        This function has to be modified to accept more authors
    Arguments :
        word: the word that we want to study
    Return :
        The author's last name
    """
    listOfMentioners = findAuthorsWhoMentioned(word).keys()
    if listOfMentioners == [] :
        return "Aucun préseident n'a parlé de",word,"Dans ses discours."
    elif "Giscard dEstaing" in listOfMentioners :
        return "Giscard dEstaing"
    elif "Mitterand" in listOfMentioners :
        return "Mitterand"
    elif "Chirac" in listOfMentioners :
        return "Chirac"
    elif "Sarkozy" in listOfMentioners :
        return "Sarkozy"
    elif "Hollande" in listOfMentioners :
        return "Hollande"
    elif "Macron" in listOfMentioners :
        return "Macron"
    
def createWhoseTextIsIt(directory = "./cleaned/") -> dict:
    """ Creates a dictionary used to interpret the TF-IDF matrix
        Associates with each author the indexes corresponding to his texts
    Argument :
        directory (optional) : the directory that contains the corpus of cleaned documents
    Return :
        textIndex : keys : the authors' last names
                    values : the index of the corresponding columns in the TF-IDF matrix 
    """
    textIndex = {}
    filesOfTheFolder = listdir(directory)
    for i in range(len(filesOfTheFolder)):
        authorsName = findAuthorsName(filesOfTheFolder[i])
        if authorsName in textIndex.keys():
            textIndex[authorsName].append(i + 1)
        else:
            textIndex[authorsName] = [i + 1]
    return textIndex

def allAuthorsSaid(directory = "./cleaned/") -> list:
    """ Creates a list of all words that all authors said and that are not useless words
    Arguments :
        directory (optional) : the directory that contains the corpus of cleaned documents
    Return :
        result : the list of all words that all authors said and that are not useless words
    """
    tfidfMatrix = createTfidfMatrix(directory)
    whoseTestItIs = createWhoseTextIsIt(directory)
    trashWords = createUselessWordsList(directory)
    result = []
    for row in tfidfMatrix:
        saidByAll = True
        authorsList = list(whoseTestItIs.keys())
        authorIndex = 0
        while saidByAll and authorIndex < len(authorsList):
            saidByAll = False
            for i in whoseTestItIs[authorsList[authorIndex]]:
                if row[i] != 0:
                    saidByAll = True
            authorIndex += 1
        if saidByAll and row[0] not in trashWords:
            result.append(row[0])                                            # le mot étudié (qui est à l'indice 0 de la ligne)
    return result