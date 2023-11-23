import os
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


def conversion_min (list_doc) :
    os.mkdir("cleaned")
    print(list_doc)
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
                    print(i)
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
    print(chaine_de_caractere)
    for i in range(len(chaine_de_caractere)):
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
    print(dictionnaire)
    del dictionnaire[""]
    return dictionnaire

def matrice_idf(dico_entrant):
    nombre_apparition={}
    for matrice_tf in dico_entrant.values():
        for cle in matrice_tf.keys():
            if cle in dico_sortant.keys():
                dico_sortant[cle]=+1
            else:
                dico_sortant[cle]=1
