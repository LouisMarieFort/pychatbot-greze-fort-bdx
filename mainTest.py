from dataPreprocessingFunctions import *
from authorManagementFunctions import *
from tfidfFunctions import *
from questionRepresentationFunctions import *
from checkFunctions import *
from questionManagement import *

# Traitement des fichiers du dossier speeches
for fileName in listdir("./speeches/"):
        createCleanedFile(fileName)
        removeFilePunctuation(fileName)

# Ecrire ci-dessous les tests à effectuer qui ne seront pas enregistrés sur Git

