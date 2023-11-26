from function import *

directory = "./speeches"
files_names = list_of_files(directory, "txt")

#récupération des noms des présidents
liste_nom=[]
for name in files_names :
    if nom_president(name) not in liste_nom :
        liste_nom.append(nom_president(name))

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

#Création d'un dictionnaire prenant en clé le nom des textes et associant à chacun d'eux un dictionnaire contenant le score TF-IDF de chacun des mots
dico_matrice_tf_idf=(matrice_tf_idf(dictionnaire_speech,dico_matrice_idf))
print(dico_matrice_tf_idf)
def Fonctionnalité () :
    num=int(input("A quel fonctionnalité souhaitez vous accéder ?\n "
                  "Pour la fonctionnalité 1 : taper 1 \n"
                  "Pour la fonctionnalité 2 : taper 2 \n"
                  "Pour la fonctionnalité 3 : taper 3 \n"
                  "Pour la fonctionnalité 4 : taper 4 \n"
                  "Pour la fonctionnalité 5 : taper 5 \n"
                  "Pour la fonctionnalité 6 : taper 6 "))
    while num <1 or num > 6 :
        num=int(input("Cette fonctionnalité n'est pas disponible veuillez donner un numéro entre 1 et 6 inclus !"))

    if num == 1  : #Fonctionnalité 1
        print("La liste des mots non important est : ",list_mot_non_important(files_names, dico_matrice_tf_idf))  #Fonctionnalité 1

    if num == 2  : #Fonctionnalité 2
        if len(Tf_Idf_elever(files_names, dico_matrice_tf_idf)) ==1 :
            print("Le mot ayant le score TD-IDF le plus élever est :",Tf_Idf_elever(files_names, dico_matrice_tf_idf))
        else :
            print("Les mots ayant le score le plus élever sont :",Tf_Idf_elever(files_names, dico_matrice_tf_idf))

    if num == 3 : #Fonctionnalité 3
        texte1=mot_le_plus_repeter("Nomination_Chirac1.txt",dictionnaire_speech)
        texte2= mot_le_plus_repeter("Nomination_Chirac2.txt",dictionnaire_speech)
        if texte1[1] > texte2[1] :
            if len(texte1[0]) == 1:
                print("Le mot le plus répeter par Chirac est :",texte1[0])
            else :
                print("Les mots le plus répeter par Chirac sont :", texte1[0])
        elif texte1[1] == texte2[1] :
            print("Les mots les plus répeter par Chirac sont :", texte1[0]+texte2[0])
        else :
            if len(texte2[0]) == 1 :
                print("Le mot le plus répeter par Chirac est :", texte2[0])
            else :
                print("Les mots le plus répeter par Chirac sont :", texte2[0])
    if num == 4 : #Fonctionnalité 4
        dico=Trouver_mot("nation",dictionnaire_speech,files_names)
        max=0
        Liste=[]
        for i in dico.items() :
            Liste.append(i[0])
            if i[1] > max :
                max = i[1]
                nom = i[0]
        if len(Liste) > 0 :
            print("Les présidents qui ont utilisé le mot 'Nation' sont :",Liste," et le president qui a le plus utilisé le mot 'Nation' est : ",nom)
        else :
            print("Aucun président n'a utilisé le mot Nation")
    if num == 5 : #Fonctionnalité 5
        if premier_ecologiste(dictionnaire_speech) == False :
            print("Aucun president n'a parlé d'écologie")
        else :
            print("Le premier president à avoir parler d'écologie est :",premier_ecologiste(dictionnaire_speech))
    if num == 6 : #Fonctionnalité 6
        print("Hormis les mots dits « non importants »les mots répété par tous sont :",mot_répété_par_tous(dico_matrice_idf))

Fonctionnalité()

