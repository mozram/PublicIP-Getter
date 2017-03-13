import os
import ipgetter
                                                                                                                         
path = '/home/pi/data/syncaod/Sharing/' #Change this path to a location where you want the ip saved.
myip = ipgetter.myip()                                                                                                   
filename = myip + '.ip'
print('Current WAN IP is ' + myip)  #You may want to disable this. If you run this script in background it will saved to root mail.
for file in os.listdir(path):
 if file.endswith('.ip'):
  os.rename('/home/pi/data/syncaod/Sharing/' + file,'/home/pi/data/syncaod/Sharing/' + filename)
  #Find the file with .ip extension and update it to new ip.
