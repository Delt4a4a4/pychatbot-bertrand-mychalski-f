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
def nom_president (list_doc) :
    list_name= []
    for i in range(len(list_doc)) :
        j=11 #commencement a 11 pour éviter Nomination_
        x= str()
        while (ord(list_doc[i][j]) > 96 and ord(list_doc[i][j]) < 123) or (ord(list_doc[i][j]) > 64 and ord(list_doc[i][j]) < 91) or ord(list_doc[i][j]) == 32 :
            x+= list_doc[i][j]
            j+=1
        if x not in list_name : #verification pour ne pas mettre de doublon
            list_name.append(x)
    return list_name

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

def suppression_ponctuation (list_doc) :
    for i in list_doc :
        with open("cleaned/"+i,"r") as f :
            content = f.readlines()
        with open("cleaned/" + i, "w") as f:
            for i in content :
                f.write(ponctuation(i))

def conversion_lettre (list_texte) :
    for i in list_texte :
        with open ("cleaned/"+i,"r") as f :
            content = f.readlines()
        with open ("cleaned/"+i,"w") as f :
            for line in content :
                chaine=""
                for i in line :
                    if i == "Ã" :
                        chaine += ""
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
        dico_sortant[key]=math.log(1/(dico_sortant[key]/len(dico_entrant)))
    return dico_sortant
        
def matrice_tf_idf(integral_dico_tf,dico_idf):
    score_tf_idf={}
    for nom_texte in integral_dico_tf.keys():
        score_tf_idf_par_texte={}
        for mot in integral_dico_tf[nom_texte].keys():
            score_tf_idf_par_texte[mot]=integral_dico_tf[nom_texte][mot]*dico_idf[mot]
        score_tf_idf[nom_texte]=score_tf_idf_par_texte
    return score_tf_idf

#Fonctionnalité 1 :
def list_mot_non_important(file_name,dico_tf_idf) :
    Liste = []
    for i in file_name :
        for j in dico_tf_idf[i].items() :
            if j[1] == 0 :
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
                print(max)
            if j[1] == max and j[0] not in Liste :
                Liste.append(j[0])
    return Liste


            
            
