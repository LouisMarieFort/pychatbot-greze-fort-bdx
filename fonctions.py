from os import path

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

def president_first_name(secondName: str):
    presidents = {"Chirac": "Jacques", "Giscard d'Estaing": "Valéry", "Mitterrand": "François", "Macron": "Emmanuel", "Sarkozy": "Nicolas"}
    if secondName in presidents.keys():
        return presidents[secondName]
    print("Ce président n'est pas enregistré.")
    return None

def president_list_display():
    """Display the list of the presidents' name. Return None"""
    print("Jacques Chirac", "Valéry Giscard d'Estaing", "François Mitterrand", "Emmanuel Macron", "Nicolas Sarkozy")
    return None

def create_cleaned_file(fileName: str):
    file = open("./speeches/" + fileName, 'r', encoding='UTF-8')
    cleanedFile = open("./cleaned/" + fileName, 'w', encoding='UTF-8')
    for line in file.readlines():
        cleanedFile.write(line.lower())