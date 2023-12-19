from re import sub

def createCleanedFile(fileName: str, directory = "./speeches/") -> None:
    """ Duplicate the file in the folder cleaned
    Argument :
        fileName : the name of the file that we want to clean
        directory : the name of the directory where we want the cleaned file
    Return None
    """
    file = open(directory + fileName, 'r', encoding = "UTF-8")
    cleanedFile = open("./cleaned/" + fileName, 'w', encoding = "UTF-8")
    for line in file.readlines():
        cleanedFile.write(line.lower())
    file.close()
    cleanedFile.close() 

def removeFilePunctuation(fileName: str, directory = "./cleaned/") -> None:
    """ Remove the punctuation in the text file which is in the folder cleaned
    Argument :
        fileName : the name of the file that we want to clean
    Return None
    """
    punctuation = {'\n', '!', ',', '?', ';', '"', '’'}
    specificPunctuation = {'-', "'", '.', ',\n'}
    file = open(directory + fileName, 'r', encoding = "UTF-8")
    text = file.read()
    for punctuationMark in specificPunctuation:
       text = text.replace(punctuationMark, ' ')    
    for punctuationMark in punctuation:
        text = text.replace(punctuationMark, '')
    text = sub(' +', ' ', text)
    if text[-1] == ' ':
        text = text[:-1]
    file.close()
    file = open(directory + fileName, 'w', encoding = "UTF-8")
    file.write(text)
    file.close()

def manageSimilarWords(fileName : str, directory = "./cleaned/") -> None:
    text = open(directory + fileName, 'r', encoding = "UTF-8").read()
    correspondingWord = {" le ": {" l ", " la "}, " que " : {" qu "}, " je " : {" j "}}
    for word in correspondingWord.keys():
        for elidedWord in correspondingWord[word]:
            text = text.replace(elidedWord, word)
    file = open(directory + fileName, 'w', encoding = "UTF-8")
    file.write(text)
    file.close()

def removeAccents(fileName : str, directory = "./cleaned/") -> None:
    text = open(directory + fileName, 'r', encoding = "UTF-8").read()
    correspondingLetter = {'a': {'à', 'â', 'ä'}, 'e': {'é', 'è', 'ê', 'ë'}, 'i': {'î', 'ï'}, 'o': {'ô', 'ö'}, 'u': {'ù', 'û', 'ü'}}
    for letter in correspondingLetter.keys():
        for accentuatedLetter in correspondingLetter[letter]:
            text = text.replace(accentuatedLetter, letter)
    file = open(directory + fileName, 'w', encoding = "UTF-8")
    file.write(text)
    file.close()