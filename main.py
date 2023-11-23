from function import *

directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)

#afficher les prénoms des présidents
list_name=nom_president(files_names)
print(list_name)
#afficher les prénoms
print(prenom(list_name))

#transferer les fichiers
conversion_min(files_names)

#enlever les ponctuations
suppression_ponctuation(files_names)
conversion_lettre(files_names)
dictionnaire_speech = {}
for i in files_names :
    print(i)
    with open("cleaned/" + i, "r") as f:
        content = f.readlines()
        dictionnaire_speech[i]= occurence_matrice_tf(str(content))

for texte in files_names:
    dico=dictionnaire_speech[texte]

print(matrice_idf(dictionnaire_speech))

