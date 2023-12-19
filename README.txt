# My first ChatBot

Réalisé par **Adam Greze** et **Louis-Marie Fort**

>Lien GitHub : https://github.com/LouisMarieFort/pychatbot-greze-fort-bdx



  ## Fonctionnalités principales :
  
Ceci est la liste des fonctions que l’utilisateurs pourra utiliser pour obtenir un résultat clair ordonné et facile d’utilisation.

* createUselessWordsList() : Cette fonction nous permet d’afficher la liste des mots les moins importants du corpus de documents lorsqu’elle est appelée.

* createHigherTFidfWordsList() : Cette fonction nous permet d’afficher le(s) mot(s) ayant le score TF-IDF le plus élevé.

* mostRepeatedWords() : Cette fonction permet a l’utilisateur d’afficher le(s) mot(s) le(s) plus répété(s) par un auteurs.

* findAuthorsWhoMentioned() : Cette fonctionnalité permet d’afficher le(s) nom(s) du (des) auteur(s) qui a (ont) parlé d'un certain mot.

* findAuthorsWhoMostRepeated() : Cette fonctionnalité permet d’afficher le(s) nom(s) du (des) auteur(s) qui a (ont) le plus parlé d'un certain mot.

* findFirstToMention() : Cette fonctionnalité permet d’afficher le(s) premier(s) président(s) à parler d'un certain mot.

* allAuthorsSaid() : Cette fonction permet à l’utilisateur d’afficher les mots que tous les auteurs ont répété et qui ne sont pas 'moins importants'.

* MostRelevantSentence() : Cette fonction permet de renvoyer la phrase la plus 'intéressante' dans le corpus de document à l'utilisateur.



  ## Fonctionnalités techniques :

Ceci est la liste des fonctions plus techniques, permettant à l’utilisateur d’obtenir un résultat ‘brut’, non traité mais offrant généralement une grande quantité de données, ou des fonctions intermédiaires permettant l’obtention des résultats finaux.

* findAuthorsName() : Cette fonctions permet d’afficher le nom de l'auteur à partir du nom d'un fichier texte.

* findAuthorsFirstName() : Cette fonctions permet à l’utilisateur d’afficher le prénom correspondant au nom d'un auteur.

* authorsListDisplay() : Cette fonction permet d’afficher la liste des noms des auteurs.

* createCleanedFile() : Cette fonction permet de créer les versions 'nettoyés' des fichiers texte , c’est-à-dire des texte sans majuscules, ni accents juste avec ponctuations et espaces.

* removeFilePunctuation() : Cette fonction permet de supprimer la ponctuation des fichiers 'nettoyés', laissant au final un document texte de mots en minuscules séparés par des espaces.

* termFrequency() : Cette fonction permet d’afficher le dictionnaire TF d'un texte, c’est-à-dire le nombre d’occurrences de chaque mot du texte.

* inverseDocumentFrequency() : Cette fonction permet d’afficher le dictionnaire IDF du répertoire speeches.

* createTfidfMatrix() : Cette fonction permet d’afficher la matrice TF-IDF du répertoire speeches.

* getLoweredString() : Cette fonction permet de transformer une chaine de caractères en minuscules.

* getStringWords() : Cette fonction permet d'obtenir les mots séparés d'une chaine de caractère sous forme de liste.

* getCleanedQuestion() : Cette fonction permet de retourner la version 'nettoyées' de la question entrée.

* getIntersectionWords() : Cette fonction permet d'obtenir tout les mots qui sont présents à la fois dans le corpus de texte et dans la question.

* getQuestionTf() : Similaire à la fonction termFrequency(), celle-ci permet d'obtenir le nombre d'occurence de chaque mot.

* getQuestionTfidfMatrixSimilaire() : à la fonction createTfidfMatrix(), cette fonction permet d’afficher la matrice TF-IDF du répertoire speeches.

* highestTfidfOfQuestion() : Cette fonction permet d'afficher le ou les mots avec le score tf idf les plus élevés.



  ## Instruction d'utilisation du programme :

Le plus simple est de lancer le programme main.py et de suivre les instructions du menu dans la console.
Il est aussi possible, avec une bonne connaissance du projet, de réaliser des programmes utilisant les fonctions disponible directement dans le fichier mainTest.py.
