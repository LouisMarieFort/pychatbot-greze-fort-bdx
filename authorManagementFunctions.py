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
    authors = {"Chirac": "Jacques", "Giscard dEstaing": "Valéry", "Hollande": "François", "Mitterrand": "François", "Macron": "Emmanuel", "Sarkozy": "Nicolas"}
    if lastName in authors.keys():
        return str(authors[lastName])
    print("Ce président n'est pas enregistré.")

def DisplayAuthorsList(directory = "./speeches/") -> None:
    """ Display the list of the authors' names. Return None"""
    listOfPresidentsNames = []
    for fileName in listdir(directory):
        fullName =  findAuthorsFirstName(findAuthorsName(fileName)) + ' ' + findAuthorsName(fileName)
        if fullName not in listOfPresidentsNames:
            listOfPresidentsNames.append(fullName)
    print(listOfPresidentsNames)