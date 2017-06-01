#!/usr/bin/env python3

"""
    usage : unzip unFichierZippé.zip

    Un exemple simple de scripting en ligne de commande.
    Prend en argument le nom d'une archive zippée (fichier.zip).
    Extrait les fichiers et les sauvegarde dans des sous-répertoires
    par nom d'extension.

"""

# import des modules et fonctions python dont nous avons besoin
from sys import argv as arguments
from os.path import exists, isdir
from os import mkdir
from shutil import rmtree
import zipfile

""" s'il n'y a pas exactement deux elements qui compose la ligne
    de commande, on est certain que la commande est incorrecte """
if len(arguments) != 2:
    print("""attention : mauvaise utilisation de la commande.\n
          unzipbytype requiert exactement un argument:\n \
           unzipbytype fichier.zip """)
    exit(None)


ZIPFILENAME = arguments[1]
# plus besoin d'afficher le nom du fichier
# print('le fichier à manipuler est : ', ZIPFILENAME)

if not ZIPFILENAME.endswith('.zip'):
    ### ce n'est pas un fichier zip : test insufisant
    ### mais pour un début : on se contente de ce test
    print("le fichier : ", ZIPFILENAME, "n'est pas un fichier zip")
    exit(1)

elif not exists(ZIPFILENAME):
    #  le fichier à manipuler n'existe pas
    print(ZIPFILENAME, "n'est pas un fichier existant")
    exit(2)

elif not zipfile.is_zipfile(ZIPFILENAME):
    """ le programme de manipulation des fichiers zip
        a échouer à ouvrir le fichier en argument """
    print("l'archive : ", ZIPFILENAME, "est non reconnue comme intégre")
    exit(3)

else:
    # on peut traiter le fichier et extraire les fichiers
    DIRECTORY_NAME = ZIPFILENAME[:-4]
#    with zipfile.ZipFile(ZIPFILENAME, 'r') as ZIP_FILE_OBJECT:

        # supprimer le répertoire destination s'il existe


        # avant de pouvoir le créer

        # plus besoin d'afficher ceci
        #print("le repertoire principal : ", DIRECTORY_NAME, " a été créé")

 #       LIST_OF_FILES = ZIP_FILE_OBJECT.filelist

 #       DICO_EXT ={}

 #       for FICHIER in LIST_OF_FILES:

            # le nom est le dernier élément du chemin absolu
            # print(FICHIER.filename)
#            FICHIER_NAME = FICHIER.filename.split('/')[-1]

           # plus besoin d'afficher cela
           # print(FICHIER.filename)
           # print(FICHIER.filename.split('/'))

#            if FICHIER_NAME == '':
                # fichier courant : répertoire, passer au suivant sans rien faire

#            else:
                # on a faire à un fichier régulier


                    # l'extension est ce qui suit le dernier .


                # si le répertoire destination existe déja, alors : pas besoin de le créer


                # le fichier à créer est un fichier binaire

                # récuperer le contenu du fichier courant depuis l'archive

                # ne pas oublier la fermeture du fichier

    # ouverture du fichier de log


    # comptage des nombres de fichiers par extension
#    for extension in DICO_EXT:

        # affichage à l'écran

        # écriture du fichier de log

    # fermeture du fichier de log

    # code de retour de fonction: tout s'est bien passé
