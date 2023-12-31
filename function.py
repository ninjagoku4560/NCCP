import os




commandeDispo = ["help","requests","exit","options"]
commandeDescriptionEn_us =["","send request by using requests library.","leave the console",""] 
commandeDescriptionFr_fr =["","Permet d'envoyer des requetes en uilisant la librairie 'requests'","Ferme la console",""] 

faconcommandeEn_us = ["","requests (enter type of request) (enter url) (if type is get put here what you want to display)","","options lang set/show en_us/fr_fr"]
faconcommandeFr_fr = ["","requests (entrer un type de requetes) (entrer un url) (si le type est 'get' mettez ici comment vous voulez que la reponse soit afficher)","","options lang set/show en_us/fr_fr"]

nbrCommande = 4

language = "en_us"


def findCommand(input):
    global language
    commande = input.split(" ")
    temp = None
    i = 0
    while True:
        temp = commandeDispo[i]
        if temp == commande[0]:
            return i
        elif nbrCommande == i:
            if language == "en_us":
                print("Command not found")
            elif language == "fr_fr":
                print("Commande non trouve")
            break
        else:
            i += 1
            
    
    
def help():
    i = 1
    while i<nbrCommande:
        global language
        if language == "en_us":
            print(commandeDispo[i]+": ")
            print(commandeDescriptionEn_us[i])
            print(faconcommandeEn_us[i])
        elif language == "fr_fr":
            print(commandeDispo[i]+": ")
            print(commandeDescriptionFr_fr[i])
            print(faconcommandeFr_fr[i])
        i+=1
       
def requests(commande):
    global language
    try:
       import requests
       command = commande.split(" ")
       type = command[1]
       url = command[2]
       moreoptions = command[3]
       if type == "get":
           r = requests.get(url)
           if moreoptions == "text":
               print(r.text)
           elif moreoptions == "content":
               print(r.content)
           elif moreoptions == "json":
               import json
               print(r.json)
       elif type == "post":
           r = requests.post(url)
       elif type == "put":
           r = requests.put(url)
       elif type == "delete":
           r = requests.delete(url)
       elif type == "head":
           r = requests.head(url)
       elif type == "options":
           r = requests.options(url)
       else:
           if language == "en_us":
               print("Request type not supported or non-existent")
           elif language == "fr_fr":
               print("Le type de requete est non fonctionnel ou non existante")
    except:
       print("Error")



def exit():
    global language
    if language == "en_us":
      print("Good bye")
    elif language == "fr_fr":
        print("Au revoir")

    
    
def math(calcul):
    return int(calcul)


def options(Input):
    global language
    command = Input.split(" ")
    option = command[1]
    modif = command[2]
    try:
        newValue = command[3]
    except:
        newValue = None
    
    if option == "lang":
        if modif == "show":
            if language == "en_us":
                print("The langage is", language)
            elif language == "fr_fr":
                print("La langue est",language)
            else:
                print("error")
                print("reset variable language")
                language = "en_us"
        elif modif == "set":
            if newValue == "en_us" or newValue == "fr_fr":
                language = newValue
            else:
                if language == "en_us":
                    print("Unknown or unimplanted language")
                elif language == "fr_fr":
                        print("Langue inconnue ou non implante")
