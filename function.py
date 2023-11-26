import os
import math
#fonction pour récuperer les noms des docs
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

#fonction pour extraire les noms des présidents
def nom_president (nom_texte) :
    j=11 #commencement a 11 pour éviter Nomination_
    x= str()
    while (ord(nom_texte[j]) > 96 and ord(nom_texte[j]) < 123) or (ord(nom_texte[j]) > 64 and ord(nom_texte[j]) < 91) or ord(nom_texte[j]) == 32 :
        x+= nom_texte[j]
        j+=1
    return x

def prenom (list_name) :
    L=[]
    for i in list_name :
        if i == "Macron" :
            L.append("Emmanuel"+" " + i)
        elif i == "Chirac" :
            L.append("Jacques" + " " + i)
        elif i == "Sarkozy" :
            L.append("Nicolas" + " " + i)
        elif i == "Mitterrand" or i=="Hollande" :
            L.append("François" + " " + i)
        elif i == "Giscard dEstaing" :
            L.append("Valéry" + " " + i)
    return L

#Fonction qui crée un nouveau dossier contenant les textes du dossier speeches tout en minuscule
def conversion_min (list_doc) :
    #os.mkdir("cleaned")
    for i in list_doc :
        with open("speeches/" + i, "r") as f1,open("cleaned/"+i,"w") as f2:
                content = f1.readlines()
                for i in content :
                    for j in range(len(i)) :
                        if i[j] >= "A" and i[j]<= "Z" :
                            i = i.replace(i[j],chr(ord(i[j])+32),1)
                    f2.write(i)

#Fonction qui supprime la ponctuation dans un texte
def ponctuation (line) :
    ponctuation1= "!:,.?;()/\_*\n-'[]"
    chaine=""
    for i in line :
        if i not in ponctuation1 :
            chaine+= i
        elif i in "'-.\n":
            chaine += " "
        else :
            chaine += ""
    return chaine

#Fonction qui supprime la ponctuation de tout les textes en utilisant la fonction ponctuation
def suppression_ponctuation (list_doc) :
    for i in list_doc :
        with open("cleaned/"+i,"r") as f :
            content = f.readlines()
        with open("cleaned/" + i, "w") as f:
            for i in content :
                f.write(ponctuation(i))

#Fonction qui convertit les caractères spéciaux en caractères avec un code ascii entre 97 et 122
def conversion_lettre (list_texte) :
    for i in list_texte :
        with open ("cleaned/"+i,"r") as f :
            content = f.readlines()
        with open ("cleaned/"+i,"w") as f :
            for line in content :
                chaine=""
                for i in line :
                    if i == "§" : #ç
                        chaine+= "c"
                    elif i in "©ª¨ë" : #éêè
                        chaine += "e"
                    elif i in "â¢" : #à
                        chaine += "a"
                    elif i == "¹" : #ù
                        chaine += "u"
                    elif i == " " :
                        chaine += " "
                    elif i>="a" and i<= "z" :
                        chaine += i
                f.write(chaine)

def occurence_matrice_tf(chaine_de_caractere):
    mot=""
    dictionnaire={}
    for i in range(2,len(chaine_de_caractere)-2): #commencement a 2 et fin a -2 pour éviter les crochets et les guillements de début et de fin
        if chaine_de_caractere[i]==" ":
            if mot in dictionnaire:
                dictionnaire[mot]+=1
            else:
                dictionnaire[mot]=1
            mot=""
        elif i==len(chaine_de_caractere)-1:
            mot = mot + chaine_de_caractere[i]
            if mot in dictionnaire:
                dictionnaire[mot]+=1
            else:
                dictionnaire[mot]=1
            mot=""
        else:
            mot=mot+chaine_de_caractere[i]
    del dictionnaire[""]
    return dictionnaire

def matrice_idf(dico_entrant):
    dico_sortant={}
    for matrice_tf in dico_entrant.values():
        for cle in matrice_tf.keys():
            if cle in dico_sortant.keys():
                dico_sortant[cle]+=1
            else:
                dico_sortant[cle]=1
    for key in dico_sortant.keys():
        dico_sortant[key]=math.log10((len(dico_entrant)/dico_sortant[key])+1)
    return dico_sortant
        
def matrice_tf_idf(integral_dico_tf,dico_idf):
    """
    entrée : 
        - (integral_dico_tf) : dictionnaire associant à chaque nom de texte un dictionnaire associant à chaque mot son score TF
        - (dico_idf) : dictionnaire associant à chaque mot son score IDF
    sortie :
        - (score_tf_idf) : dictionnaire associant à chaque nom de texte un dictionnaire associant à chaque mot son score TF-IDF
        
    Description :
        - La fonction parcours pour chaque dictionnaire TF(inscrit en valeur) associé à chaque texte(inscrit en clé) l'ensemble des mots et multiplie le score TF
        par le score IDF (à l'aide du mot qui sert de clé aussi dans le dictionnaire IDF) et inscrit le score TF-IDF ainsi obtenu dans un nouveau dictionnaire qui 
        à chaque nom de fichier (la clé) associe un dictionnaire(la valeur) contenant le score TF-IDF de chaque mot.
    """
    score_tf_idf={} # initialisation du dico qui va être retourné
    for nom_texte in integral_dico_tf.keys(): # parcour le nom des textes enregistrés en clés dans le dico contenant les dico TF de chaque texte
        score_tf_idf_par_texte={} # initialisation des dicos TF-IDF de chaque texte
        for mot in integral_dico_tf[nom_texte].keys(): # parcour les mots enregistré en clé de chaque sous-dico
            score_tf_idf_par_texte[mot]=integral_dico_tf[nom_texte][mot]*dico_idf[mot] # multiplie le score TF par le score IDF et enregistre le score TF-IDF dans un sous-dico
        score_tf_idf[nom_texte]=score_tf_idf_par_texte # enregistre les dico des scores tf idf par texte dans le dico les contenants tous
    return score_tf_idf # retournement du dico obtenu

#Fonctionnalité 1 :
def list_mot_non_important(file_name,dico_tf_idf) :
    Liste = []
    for i in file_name :
        for j in dico_tf_idf[i].items() :
            if j[1] == math.log10(2) :
                if j  not in Liste :
                    Liste.append(j[0])
    return Liste

def Tf_Idf_elever (file_name,dico_tf_idf) :
    Liste = []
    max = 0
    for i in file_name :
        for j in dico_tf_idf[i].items() :
            if j[1] > max :
                Liste=[]
                Liste.append(j[0])
                max = j[1]
            if j[1] == max and j[0] not in Liste :
                Liste.append(j[0])
    return Liste

def mot_le_plus_repeter (nom_president,dico_speeche) :
    max=0
    mot=[]
    for i in dico_speeche[nom_president].items() :
        if i[1] > max :
            max = i[1]
            mot=[]
            mot.append(i[0])
        elif i[1] == max :
            mot.append(i[0])
    return mot,max

def Trouver_mot (mot,dico_speech,file_name) :
    Dico_President_occurence = {}
    for i in file_name :
        if mot in dico_speech[i].keys() :
            Dico_President_occurence[nom_president(i)] = dico_speech[i][mot]
    return Dico_President_occurence

def mot_répété_par_tous(dico_idf):
    mots_non_importants=["au", "aux", "avec", "ce", "ces", "dans", "de", "des", "du", "elle", "en", "et", "eux", "il", "ils",
    "je", "la", "le", "les", "leur", "lui", "ma", "mais", "me", "meme", "mes", "moi", "mon", "ne", "nos",
    "notre", "nous", "on", "ou", "par", "pas", "pour", "qu", "que", "qui", "sa", "se", "ses", "son", "sur",
    "ta", "te", "tes", "toi", "ton", "tu", "un", "une", "vos", "votre", "vous", "c", "d", "j", "l", "a","m",
    "m", "n", "s", "t", "y", "ete", "etee", "etees", "etes", "etant", "etante", "etants", "etantes", "suis",
    "es", "est", "sommes", "etes", "sont", "serai", "seras", "sera", "serons", "serez", "seront", "serais",
    "serait", "serions", "seriez", "seraient", "etais", "etait", "etions", "etiez", "etaient", "fus", "fut",
    "fumes", "futes", "furent", "sois", "soit", "soyons", "soyez", "soient", "fusse", "fusses", "fut",
    "fussions", "fussiez", "fussent", "ayant", "ayante", "ayantes", "ayants", "eu", "eue", "eues", "eus",
    "ai", "as", "avons", "avez", "ont", "aurai", "auras", "aura", "aurons", "aurez", "auront", "aurais",
    "aurait", "aurions", "auriez", "auraient", "avais", "avait", "avions", "aviez", "avaient", "eut",
    "eumes", "eutes", "eurent", "aie", "aies", "ait", "ayons", "ayez", "aient", "eusse", "eusses", "eut",
    "eussions", "eussiez", "eussent"]
    liste_mot=[]
    for mot in dico_idf.keys():
        if dico_idf[mot]==math.log10(2) and dico_idf[mot] not in mots_non_importants:
            liste_mot.append(mot)
    return liste_mot


def premier_ecologiste(dico_ensemble_itf):
    ordre_textes=[
                "Nomination_Giscard dEstaing.txt",
                "Nomination_Chirac1.txt","Nomination_Chirac2.txt",
                "Nomination_Mitterrand1.txt", "Nomination_Mitterrand2.txt",
                "Nomination_Sarkozy.txt",
                "Nomination_Hollande.txt",
                "Nomination_Macron.txt"]
    lexique_ecologie = ["ecologie", "climat"]
    for indice_texte in range(len(ordre_textes)) :
        for mot in lexique_ecologie:
            if mot in dico_ensemble_itf[ordre_textes[indice_texte]].keys():
                if indice_texte == 1:
                    president = "Valérie Giscard d'Estaing"
                elif indice_texte == 2 or indice_texte == 3:
                    president = "Jacques Chirac"
                elif indice_texte == 4 or indice_texte == 5:
                    president = "François Mitterand"
                elif indice_texte == 6:
                    president = "Nicolas Sarkozy"
                elif indice_texte == 7:
                    president = "Francois Hollande"
                else :
                    president = "Emmanuel Macron"
                return president
    return False
