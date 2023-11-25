from fonctions import *

userResponse = -1
numberOfPossibleResponses = 14
valable = list(range(1, numberOfPossibleResponses + 1)) ; print(valable)
"""
while reponse not in valable :
    reponse = int(input("Faites votre choix : \n 1 : Obtenir le nom des auteurs \n 2 : Obtenir le prénom de chaque auteur \n 3 : Lister les noms et prénoms de chaque préseident \n 4 : Créer un fichier 'nettoyé' de chaque discours présidentiel \n 5 : Enlever toutes les ponctuations des fichiers \n 6 : Obtenir la fréquence de chaque mot dans un fichier \n 7 : Calculer l'importance d'un terme dans l'ensemble des documents \n 8 : Accéder à la matrice affichant l'importance de tout les mots à travers tout les textes \n 9 : Afficher les mots 'moins importants' \n 10 : Afficher les motes les 'plus importants' \n 11 : Trouver le mot le plus répeté par un auteur \n 12 : Trouver qui a parlé d'un mot spécifique et qui l'a répeté le plus de fois \n 13 : Trouver qui est le 1er président a avoir parlé de quelque chose \n 14 : Trouver quels sont les mots évoqués par tout les présidents"))

if reponse == 1 :
    print(findAuthorsName("Entrez le nom du fichier"))
elif reponse == 2 :
    print(president_first_name(input("Entrez le nom d'un président")))
elif reponse == 3 :
    ..."""