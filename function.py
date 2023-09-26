import requests, time,os


commandeDispo = ["help","requests","exit"]
commandeDescription =["","send request by using requests library","leave"] 
nbrCommande = 3

def findCommand(input):
    temp = None
    i = 0
    while True:
        temp = commandeDispo[i]
        if temp == input:
            break
        else:
            i+=1
    return i
    
def help():
    i = 1
    while i<nbrCommande:
        print(commandeDispo[i]+": ")
        print(commandeDescription[i])
        print("")
        i+=1
       
def requests():
    print("Comming soon")

def exit():
    print("Good bye")
