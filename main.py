from fonctions import *

# Test rapide des fonctions
create_cleaned_file("Nomination_Chirac1.txt")
remove_file_punctuation("Nomination_Chirac1.txt")
file = open("./cleaned/Nomination_Chirac1.txt", 'r', encoding = "UTF-8")
file = file.read()
print(term_frequency(file))