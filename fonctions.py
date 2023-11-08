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
    file = open("./speeches/" + fileName, 'r', encoding = 'UTF-8')
    cleanedFile = open("./cleaned/" + fileName, 'w', encoding = 'UTF-8')
    for line in file.readlines():
        cleanedFile.write(line.lower())

def remove_file_punctuation(fileName: str):
    punctuation = {'.', '\n', ',', '?', ';'}
    specificPunctuation = {'-', "'"}
    file = open("./cleaned/" + fileName, 'r', encoding = 'UTF-8')
    text = file.read()
    for punctuationMark in punctuation:
        text = text.replace(punctuationMark, '')
    for punctuationMark in specificPunctuation:
        text = text.replace(punctuationMark, ' ')
    file.close()
    file = open("./cleaned/" + fileName, 'w', encoding = 'UTF-8')
    file.write(text)
    file.close()

create_cleaned_file("Nomination_Chirac1.txt")
remove_file_punctuation("Nomination_Chirac1.txt")
text = "a,;bd"
text = text.replace(',', 'A')
print(text)