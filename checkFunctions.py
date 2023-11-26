from fonctions import *
from os import listdir

def checkAuthorsLastNameInput(userInput : str, directory = "./speeches/"):
    """ Check a string input from the user for an author's last name
    Argument : 
        userInput : the name that we want to check
        directory (optional) : the directory where the documents are
    Return :
        True if the name is valid
        False if the name is not valid
    """
    for fileName in listdir(directory):
        if findAuthorsName(fileName) == userInput:
            return True
    return False

def checkWordExistence(userInput : str):
    """ Check a string input from the user for a word that appears in the cleaned files
    Argument : 
        userInput : the word that we want to check
    Return :
        True if the word is valid
        False if the word is not valid
    """
    idfMatrix = inverseDocumentFrequency()
    for word in idfMatrix.keys():
        if userInput == word:
            return True
    return False

def checkTxtFileExistence(userInput : str, directory = "./speeches/"):
    """ Check a string input from the user for txt file name
    Argument : 
        userInput : the file name that we want to check
        directory (optional) : the directory where the documents are
    Return :
        True if the word is valid
        False if the word is not valid
    """
    for fileName in listdir(directory):
        if fileName == userInput:
            return True
    return False

def checkTxtFileNameSyntax(userInput : str):
    """ Check a string input from the user for a file name
    Argument : 
        userInput : the word that we want to check
    Return :
        True if the file name is valid
        False if the file name is not valid
    """
    if userInput[-4 : -1] != ".txt":
        return False
    underscoreSeen = False
    digitSeen = False
    for characterIndex in range(len(userInput) - 4):
        print(userInput[characterIndex])
        if underscoreSeen and digitSeen:
            if not userInput[characterIndex].isdigit():
                return False
        elif underscoreSeen:
            if userInput[characterIndex].isdigit():
                digitSeen = True
            elif not userInput[characterIndex].isalpha() and not userInput[characterIndex].isspace():
                return False
        else:
            if userInput[characterIndex].isdigit() == '_':
                digitSeen = True
            elif not userInput[characterIndex].isalpha() and not userInput[characterIndex].isspace():
                return False
        if not underscoreSeen:
            return False
        return True