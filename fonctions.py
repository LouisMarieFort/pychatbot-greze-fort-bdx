from math import log10
from re import sub
from os import listdir

def findAuthorsName(fileName: str) -> str:
    """ Return the name of the text's author
    
    fileName : the name of the file, using this format : TextTitle_[author's name][number].txt
    """
    endIndex = len(fileName) - 4                                                      # the index of the last digit of [number]
    while ord(fileName[endIndex - 1]) < 58 and ord(fileName[endIndex - 1]) > 47:
        endIndex -= 1
    beginningIndex = endIndex
    while fileName[beginningIndex - 1] != '_':
        beginningIndex -= 1
    return str(fileName[beginningIndex : endIndex])

def findAuthorsFirstName(lastName: str) -> str: 
    """ Associates the last name of an author to his first name
    Argument :
        lastName : the last name of the author
    Return the last name of the author (str)
    """
    presidents = {"Chirac": "Jacques", "Giscard dEstaing": "Valéry", "Hollande": "François", "Mitterrand": "François", "Macron": "Emmanuel", "Sarkozy": "Nicolas"}
    if lastName in presidents.keys():
        return str(presidents[lastName])
    print("Ce président n'est pas enregistré.")

def authorsListDisplay(directory = "./speeches/") -> None:
    """ Display the list of the authors' names. Return None"""
    listOfPresidentsNames = []
    for fileName in listdir(directory):
        fullName =  findAuthorsFirstName(findAuthorsName(fileName)) + ' ' + findAuthorsName(fileName)
        if fullName not in listOfPresidentsNames:
            listOfPresidentsNames.append(fullName)
    print(listOfPresidentsNames)

def createCleanedFile(fileName: str) -> None:
    """ Duplicate the file in the folder cleaned
    Argument :
        fileName : the name of the file that we want to clean
    Return None
    """
    file = open("./speeches/" + fileName, 'r', encoding = "UTF-8")
    cleanedFile = open("./cleaned/" + fileName, 'w', encoding = "UTF-8")
    for line in file.readlines():
        cleanedFile.write(line.lower())
    file.close()
    cleanedFile.close()    

def removeFilePunctuation(fileName: str) -> None:
    """ Remove the punctuation in the text file which is in the folder cleaned
    Argument :
        fileName : the name of the file that we want to clean
    Return None
    """
    punctuation = {'\n', '!', ',', '?', ';'}
    specificPunctuation = {'-', "'", '.', ',\n'}
    file = open("./cleaned/" + fileName, 'r', encoding = "UTF-8")
    text = file.read()
    for punctuationMark in specificPunctuation:
       text = text.replace(punctuationMark, ' ')    
    for punctuationMark in punctuation:
        text = text.replace(punctuationMark, '')
    text = sub(' +', ' ', text)
    if text[-1] == ' ':
        text = text[:-1]
    file.close()
    file = open("./cleaned/" + fileName, 'w', encoding = "UTF-8")
    file.write(text)
    file.close()

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
    for wordAndITF in inverseDocumentFrequency(directory).items():
        row = [wordAndITF[0]]
        for column in range(len(filesNamesList)):
            if wordAndITF[0] in listOfTF[column].keys():
                row.append(wordAndITF[1] * listOfTF[column][wordAndITF[0]])
            else:
                row.append(0)
        matrix.append(row)
    return matrix

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
    trashWords = createUselessWordsList()
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