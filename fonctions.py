from math import log10
from re import sub
from os import listdir

def findAuthorsName(fileName: str):
    """ Return the name of the text's author
    
    fileName : the name of the file, using this format : TextTitle_[author's name][number].txt
    """
    endIndex = len(fileName) - 4                                                      # the index of the last digit of [number]
    while ord(fileName[endIndex - 1]) < 58 and ord(fileName[endIndex - 1]) > 47:
        endIndex -= 1
    beginningIndex = endIndex
    while fileName[beginningIndex - 1] != '_':
        beginningIndex -= 1
    return fileName[beginningIndex : endIndex]

def findPresidentFirstName(lastName: str):
    """ Associates the last name of an author to his first name
    Argument :
        lastName : the last name of the author
    Return the last name of the author (str)
    """
    presidents = {"Chirac": "Jacques", "Giscard dEstaing": "Valéry", "Mitterrand": "François", "Macron": "Emmanuel", "Sarkozy": "Nicolas"}
    if lastName in presidents.keys():
        return presidents[lastName]
    print("Ce président n'est pas enregistré.")
    return None

def presidentListDisplay():
    """ Display the list of the presidents' name. Return None"""
    listOfPresidentsNames = ["Jacques Chirac", "Valéry Giscard dEstaing", "François Mitterrand", "Emmanuel Macron", "Nicolas Sarkozy"]
    print(listOfPresidentsNames)
    return None

def createCleanedFile(fileName: str):
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

def remove_file_punctuation(fileName: str):
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

def term_frequency(text: str):
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

def inverse_document_frequency(directory = "./cleaned/"):
    """ Create a dictionary of the inverse document frequency of each words in the texts
    Argument :
        directory (optional) : the directory that contains the corpus of documents
    Return :
        dictionary : dictionary associating each word with its IDF score
    """
    dictionary = dict()
    for fileName in listdir(directory):
        with open("./cleaned/" + fileName, 'r', encoding = "UTF-8") as currentFile:
            fileTermFrequency = term_frequency(currentFile.read())
            for word in fileTermFrequency:
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1
    for word in dictionary:
        dictionary[word] = log10(len(listdir(directory))/dictionary[word])
    return dictionary

def TFIDF_matrix(directory = "./cleaned/"):
    matrix = []
    filesNamesList = listdir(directory)
    listOfTF = []                                                            #list of dictionaries
    for fileName in filesNamesList:
        with open(directory + fileName, 'r', encoding = "UTF-8") as file:
            listOfTF.append(term_frequency(file.read()))
    for wordAndITF in inverse_document_frequency(directory).items():
        row = [wordAndITF[0]]
        for column in range(len(filesNamesList)):
            if wordAndITF[0] in listOfTF[column].keys():
                row.append(wordAndITF[1] * listOfTF[column][wordAndITF[0]])
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def createUselessWordsList(directory = "./cleaned/"):
    tfidfMatrix = TFIDF_matrix(directory)
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

def mostRepeatedWords(authorsName = "Chirac", directory = "./cleaned/"):
    filesList = []
    totalText = ""
    for file in listdir(directory):
        if findAuthorsName(file) == authorsName:
            filesList.append(file)
    for fileName in filesList:
        with open(directory + fileName, 'r', encoding = "UTF-8") as currentFile:
            totalText += ' ' + currentFile.read()
    totalTf = term_frequency(totalText)
    maximalOccurenceNumber = max(totalTf.values())
    repeatedWords = []
    for word in totalTf:
        if totalTf[word] == maximalOccurenceNumber :
            repeatedWords.append(word)
    return repeatedWords

def createHigherTfidfWordsList(directory = "./cleaned/"):
    tfidfMatrix = TFIDF_matrix(directory)
    higherTfidf = 0
    wordsList = []
    for row in range(len(tfidfMatrix)):
        if max(tfidfMatrix[row][1:]) > higherTfidf:
            higherTfidf = max(tfidfMatrix[row][1:])
            wordsList = [tfidfMatrix[row][0]]
        elif max(tfidfMatrix[row][1:]) == higherTfidf:
            wordsList.append(tfidfMatrix[row][0])
    return wordsList

def findAuthorsWhoMentioned(word: str, directory = "./cleaned/"):
    word = word.lower() 
    authorsWhoMentioned = dict()
    for fileName in listdir(directory):
        nameOfTheAuthor = findAuthorsName(fileName)
        currentFile = open(directory + fileName, 'r', encoding = "UTF-8")
        currentTF = term_frequency(currentFile.read())
        currentFile.close()
        if word in currentTF.keys():
            if nameOfTheAuthor not in authorsWhoMentioned.keys():
                authorsWhoMentioned[nameOfTheAuthor] = currentTF[word]
            else:
                authorsWhoMentioned[nameOfTheAuthor] += currentTF[word]
    return authorsWhoMentioned

def findAuthorsWhoMostRepeated(word: str, directory = "./cleaned/"):
    word = word.lower()
    authorsWhoMentioned = findAuthorsWhoMentioned(word, directory)
    maximalOccurences = max(authorsWhoMentioned.values())
    authorsWhoMostRepeated = []
    for author in authorsWhoMentioned.keys():
        if authorsWhoMentioned[author] == maximalOccurences:
            authorsWhoMostRepeated.append(author)
    return authorsWhoMostRepeated

def findFirstToMention(word) :
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
    
def createWhoseTextIsIt(directory = "./cleaned/"):
    textIndex = {}
    filesOfTheFolder = listdir(directory)
    for i in range(len(filesOfTheFolder)):
        authorsName = findAuthorsName(filesOfTheFolder[i])
        if authorsName in textIndex.keys():
            textIndex[authorsName].append(i + 1)
        else:
            textIndex[authorsName] = [i + 1]
    return textIndex

def allAuthorsSaid(directory = "./cleaned/"):
    tfidfMatrix = TFIDF_matrix(directory)
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