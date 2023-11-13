from math import log
from re import sub
from os import listdir

def authors_name(fileName: str):
    """
    Return the name of the text's author
    
    fileName : the name of the file, using this format : TextTitle_[author's name][number].txt
    """
    name = ""
    endIndex = len(fileName) - 5                                                       # the index of the last digit of [number]
    while ord(fileName[endIndex - 1]) < 58 and ord(fileName[endIndex - 1]) > 47:
        endIndex -= 1
    beginningIndex = endIndex
    while fileName[beginningIndex - 1] != '_':
        beginningIndex -= 1
    return fileName[beginningIndex : endIndex]

def president_first_name(lastName: str):
    presidents = {"Chirac": "Jacques", "Giscard d'Estaing": "Valéry", "Mitterrand": "François", "Macron": "Emmanuel", "Sarkozy": "Nicolas"}
    if lastName in presidents.keys():
        return presidents[lastName]
    print("Ce président n'est pas enregistré.")
    return None

def president_list_display():
    """Display the list of the presidents' name. Return None"""
    print("Jacques Chirac", "Valéry Giscard d'Estaing", "François Mitterrand", "Emmanuel Macron", "Nicolas Sarkozy")
    return None

def create_cleaned_file(fileName: str):
    file = open("./speeches/" + fileName, 'r', encoding = "UTF-8")
    cleanedFile = open("./cleaned/" + fileName, 'w', encoding = "UTF-8")
    for line in file.readlines():
        cleanedFile.write(line.lower())
    file.close()
    cleanedFile.close()    

def remove_file_punctuation(fileName: str):
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

def term_frequency(text: str) :
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
        dictionary[word] = log(len(listdir(directory))/dictionary[word])
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

def useless_words(directory = "./cleaned/"):
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