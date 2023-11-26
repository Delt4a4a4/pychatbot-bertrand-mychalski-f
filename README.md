# Projet pychatbot-bertrand-mychalski-f
Notre groupe est : Baptiste BERTRAND et Ronan MYCHALSKI 
Le lien est : https://github.com/Delt4a4a4/pychatbot-bertrand-mychalski-f.git

Pour accéder aux 6 fonctionnalités il suffit de lancer la fonction : fonctionnalite(), pour cela il faut écrire fonctionnalite(), aucun argument est nécessaire. Lorque la fonction est lancé vous pourrez choisir entre les 6 fonctionnalités.

Fonctionnalité 1 :
La fonction list_non_important prends en argument le nom des textes et un dictionnaire contenant la matrice tf-idf.
Elle retourne une Liste avec les mots non importants.

Fonctionnalité 2 :
La fonction Tf_Idf_elever prends en argument le noms des textes et un dictionnaire contenant la matrice tf-idf.
Elle retourne une Liste avec le/les mots avec le tf_idf le plus élever.

Fonctionnalité 3 :
La fonction mot_le_plus_repeter prends en argument le nom du texte et un dictionnaire contenant les scores idf de chaque mot.
Elle retourne le mot le plus répeter et son nombre de fois.

Fonctionnalité 4 :
La fonction Trouver_mot prends en argument le mot à rechercher, un dictionnaire contenant les scores idt de chaque mot, une liste contenant le nom des fichiers.
Elle retourne un dictionnaire avec le nom des présidents qui ont utilisé le mot et combien de fois l'ont-il utilisé.

Fonctionnalité 5 :
La fonction premier_ecologiste prends en argument un dictionnaire contenant les scores idf de chaque mot.
Elle retourne le Prénom Nom du premier président qui a parlé d'écologie/climat ou False si aucun a parlé d'écologie/climat.

Fonctionnalité 6 :
La fonction mot_répété_par_tous prends en argument la matrice idf.
Elle retourne une liste de mot qui sont répéter par tous mais qui ne sont pas "pas important".

