import requests,time,function
  
commandeDispo = ["help","requests","exit"] 
commandeDescription =["","send request by using requests library","leave"] 
  
print("MIT License")
print("Copyright (c) 2023 ninjagoku4560") 
print("NCCP:")

Close = False

while not Close:
    commandeEntrer = str(input("•••"))
    if function.findCommand(commandeEntrer) == 0:
        function.help()
    elif function.findCommand(commandeEntrer) == 1:
        function.requests()
    elif function.findCommand(commandeEntrer) == 2:
        function.exit()
        break
