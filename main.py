from fonctions import *

# Test rapide des fonctions
for file in listdir("./speeches/"):
    create_cleaned_file(file)
    remove_file_punctuation(file)
#print(inverse_document_frequency())
#print(TFIDF_matrix())
#print(createUselessWordsList())
#print(createHigherTfidfWordsList())
#print(mostRepeatedWords())
print(list(findAuthorsWhoMentioned("Nation").keys()))
print(findAuthorsWhoMostRepeated("Nation"))