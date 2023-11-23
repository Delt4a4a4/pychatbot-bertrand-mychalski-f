from function import *
directory = "./speeches"
files_names = list_of_files(directory, "txt")
print(files_names)

#afficher les prénoms des présidents
#print(nom_president(files_names))

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
print(dictionnaire_speech["Nomination_Macron.txt"])

for texte in files_names:
    dico=dictionnaire_speech[texte]


