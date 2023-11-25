from function import *

directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)

#récupération des noms des présidents
liste_nom=nom_president(files_names)

#récuperation des prénoms des présidents
liste_prenom_nom=prenom(liste_nom)

#transfère des fichiers en minuscule dans le répertoire cleaned
conversion_min(files_names)

#Suppresion de la ponctation des fichiers du répertoire cleaned
suppression_ponctuation(files_names)

#Remplacement des çèà.. par cea pour éviter des problèmes d'affichage
conversion_lettre(files_names)

#Création d'un dictionnaire contenant le score tf des mots de chaque texte
dictionnaire_speech = {}
for i in files_names :
    with open("cleaned/" + i, "r") as f:
        content = f.readlines()
        dictionnaire_speech[i]= occurence_matrice_tf(str(content))

#Création d'un dictionnaire contenant le score idf de chaque mot
dico_matrice_idf=(matrice_idf(dictionnaire_speech))

#Baptiste complète jsp comment éxpliquer mdr
dico_matrice_tf_idf=(matrice_tf_idf(dictionnaire_speech,dico_matrice_idf))

