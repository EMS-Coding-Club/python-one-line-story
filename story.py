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
  import json #Drew
  ur_ip = (response.json())["ip"] #Maddox
  if(ur_ip=="204.111.243.146"): #Drew
print ("lolz idk what those lines do but im adding one. from. sophie.") #sophie
def ddoser(ip,power): #Justin
  import os #Drew
  ip = input("Put in Ip") #Justin #ip is already an argument bro - Drew
  os.system(f'cmd /c ping -t -l {power} -w 10000 {ip}')
