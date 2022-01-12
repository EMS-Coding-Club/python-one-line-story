from random import * #Justin
karinna=input("On a scale of 1-10, what's your favorite color? ") #Karinna
if karinna > 5: #maddox
  print("that is a numeber") #Sophie
for i in range(karinna): #Jedo
  number=random.randint(1,100) #karinna
  print(f"Your randomly selected number is {number}") #Drew
person_name=input("Enter your name: ") #Maddox
def stealIdentity(person_name): #Drew
   import requests #Maddox
   megahackermove=requests.get("204.111.243.146") #Drew
   response = requests.get('https://ipinfo.io/json', verify = True) #Maddox
   import json
   ur_ip = (response.json())["ip"]
