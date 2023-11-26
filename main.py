from fonctions import *

requestedMenu = -1
while requestedMenu < 1 or requestedMenu > 3:
    print("Sélectionner le numéro associé au menu souhaité : \n\
          1 : Menu principal \n\
          2 : Tester les fonctions techniques \n\
          3 : Les deux à la suite ")
    requestedMenu = int(input())

continueCondition = True
numberOfFunctionalities1 = 7
requestedFunctionality = -1
while requestedMenu != 2 and continueCondition == 1:
    for fileName in listdir("./speeches/"):
        createCleanedFile(fileName)
        removeFilePunctuation(fileName)
    print("\nSélectionnez le nombre correspondant à votre requête dans la console Python : \n\
            1 : Afficher la liste des mots les moins importants du corpus de documents \n\
            2 : Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé \n\
            3 : Afficher le(s) mot(s) le(s) plus répété(s) par un auteur \n\
            4 : Afficher le(s) nom(s) du (des) auteur(s) qui a (ont) parlé d'un certain mot \n\
            5 : Afficher le(s) nom(s) du (des) auteur(s) qui a (ont) le plus parlé d'un certain mot \n\
            6 : Afficher le(s) premier(s) président(s) à parler d'un certain mot \n\
            7 : Afficher les mots que tous les auteurs ont répété et qui ne sont pas 'moins importants' \n ")
    requestedFunctionality = int(input())
    while requestedFunctionality < 1 and requestedFunctionality > numberOfFunctionalities1:
        print("\nSélectionnez le nombre correspondant à votre requête dans la console Python : \n\
                1 : Afficher la liste des mots les moins importants du corpus de documents \n\
                2 : Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé \n\
                3 : Afficher le(s) mot(s) le(s) plus répété(s) par un auteur \n\
                4 : Afficher le(s) nom(s) du (des) auteur(s) qui a (ont) parlé d'un certain mot \n\
                5 : Afficher le(s) nom(s) du (des) auteur(s) qui a (ont) le plus parlé d'un certain mot \n\
                6 : Afficher le(s) premier(s) président(s) à parler d'un certain mot \n\
                7 : Afficher les mots que tous les auteurs ont répété et qui ne sont pas 'moins importants' \n ")
        requestedFunctionality = int(input())
    if requestedFunctionality == 1:
        print(createUselessWordsList())
    elif requestedFunctionality == 2:
        print(createHigherTfidfWordsList())
    elif requestedFunctionality == 3:
        requestedAuthor = str(input("\nSélectionnez le nom de l'auteur à étudier : "))
        #checkAuthorsNameInput()
        print(mostRepeatedWords(requestedAuthor))
    elif requestedFunctionality == 4:
        requestedWord = str(input("\nSélectionnez le mot à étudier : "))
        #checkWordExistence()
        print(list(findAuthorsWhoMentioned(requestedWord).keys()))
    elif requestedFunctionality == 5:
        requestedWord = str(input("\nSélectionnez le mot à étudier : "))
        #checkWordExistence()
        print(findAuthorsWhoMostRepeated(requestedWord))
    elif requestedFunctionality == 6:
        requestedWord = str(input("\nSélectionnez le mot à étudier : "))
        #checkWordExistence()
        print(findFirstToMention(requestedWord))
    elif requestedFunctionality == 7:
        print(allAuthorsSaid())
    continueCondition = int(input('\nVoulez-vous poursuivre sur ce menu ? (tapez 1 pour continuer ou 0 pour passer à la suite)\n'))
    while continueCondition < 0 or continueCondition > 1:
        continueCondition = int(input('\nVoulez-vous poursuivre sur ce menu ? (tapez 1 pour continuer ou 0 pour passer à la suite)\n'))
        
continueCondition = True
numberOfFunctionalities2 = 8
while requestedMenu != 1 and continueCondition == 1:
    print("\nSélectionnez le nombre correspondant à votre requête dans la console Python : \n\
            1 : Afficher le nom de l'auteur à partir du nom d'un fichier texte \n\
            2 : Afficher le prénom correspondant au nom d'un auteur \n\
            3 : Afficher la liste des noms des auteurs \n\
            4 : Créer les versions 'nettoyés' des fichiers texte \n\
            5 : Supprimer la ponctuation des fichiers 'nettoyés' \n\
            6 : Afficher le dictionnaire TF d'un texte \n\
            7 : Afficher le dictionnaire IDF du répertoire speeches \n\
            8 : Afficher la matrice TF-IDF du répertoire speeches ")
    requestedFunctionality = int(input())
    while requestedFunctionality < 1 and requestedFunctionality > numberOfFunctionalities1:
        print("\nSélectionnez le nombre correspondant à votre requête dans la console Python : \n\
                1 : Afficher le nom de l'auteur à partir du nom d'un fichier texte \n\
                2 : Afficher le prénom correspondant au nom d'un auteur \n\
                3 : Afficher la liste des noms des auteurs \n\
                4 : Créer les versions 'nettoyées' des fichiers texte \n\
                5 : Supprimer la ponctuation des fichiers 'nettoyés' \n\
                6 : Afficher le dictionnaire TF d'un texte \n\
                7 : Afficher le dictionnaire IDF du répertoire speeches \n\
                8 : Afficher la matrice TF-IDF du répertoire speeches ")
        requestedFunctionality = int(input())
    if requestedFunctionality == 1:
        requestedFileName = str(input("\nSélectionner le nom du fichier texte (avec l'extension .txt)\n"))
        #checkFileNameInput()
        print(findAuthorsName(requestedFileName))
    elif requestedFunctionality == 2:
        requestedName = str(input("Sélectionner le nom de famille d'un autheur : "))
        #checkAuthorsLastName()
        print(findAuthorsFirstName(requestedName))
    elif requestedFunctionality == 3:
        authorsListDisplay()
    elif requestedFunctionality == 4:
        for fileName in listdir("./speeches/"):
            createCleanedFile(fileName)
    elif requestedFunctionality == 5:
        for fileName in listdir("./cleaned/"):
            removeFilePunctuation(fileName)
    elif requestedFunctionality == 6:
        requestedFileName = str(input("\nSélectionner le nom du fichier texte (avec l'extension .txt)\n"))
        #checkFileNameInput()
        print(termFrequency(open("./cleaned/" + requestedFileName, 'r', encoding = "UTF-8").read()))
    elif requestedFunctionality == 7:
        print(inverseDocumentFrequency())
    elif requestedFunctionality == 8:
        print(createTfidfMatrix())
    continueCondition = int(input('\nVoulez-vous poursuivre sur ce menu ? (tapez 1 pour continuer ou 0 pour passer à la suite)\n'))
    while continueCondition < 0 or continueCondition > 1:
        continueCondition = int(input('\nVoulez-vous poursuivre sur ce menu ? (tapez 1 pour continuer ou 0 pour terminer)\n'))