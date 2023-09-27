import os




commandeDispo = ["help","requests","exit","options"]
commandeDescription =["","send request by using requests library.","leave",""] 
faconcommande = ["","requests (enter type of request) (enter url) (if type is get put here what you want to display)","","options lang set/show en_us/fr_fr"]
nbrCommande = 4

language = "en_us"

def findCommand(input):
    commande = input.split(" ")
    temp = None
    i = 0
    while True:
        temp = commandeDispo[i]
        if temp == commande[0]:
            return i
            break
        elif nbrCommande == i:
            print("Command not found")
            break
        else:
            i=+1
    
    
def help():
    i = 1
    while i<nbrCommande:
        print(commandeDispo[i]+": ")
        print(commandeDescription[i])
        print(faconcommande[i])
        i+=1
       
def requests(commande):
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
           print("Request type not supported or non-existent")
    except:
       print("Error")



def exit():
    print("Good bye")

    
    
def math(calcul):
    return int(calcul)


def options(Input):
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
                print("The langage is ", language)
            elif language == "fr_fr":
                print("La langue est ",language)
        elif modif == "set":
            try:
                if newValue == "en_us" or newValue == "fr_fr":
                    language = newValue
                else:
                    if language == "en_us":
                        print("Unknown or unimplanted language")
                    elif language == "fr_fr":
                        print("Langue inconnue ou non implanté")
            except:
                print("error")
                        
    