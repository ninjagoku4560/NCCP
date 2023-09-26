import os


commandeDispo = ["help","requests","exit"]
commandeDescription =["","send request by using requests library.","leave"] 
faconcommande = ["","requests (enter type of request) (enter url) (if type is get put here what you want to display)",""]
nbrCommande = 3

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