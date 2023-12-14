from re import sub

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
    punctuation = {'\n', '!', ',', '?', ';', '"'}
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