#!/usr/bin/python

import socket
import sys
from datetime import datetime

banner = '''
                                    \033[91m       
                   |'.              \033[91m \033[91m
                   |  '-._        
                 .'  .._  ',     
                '   /  _'.'_\        \033[91m
               :   /  '_' '_'   
               |Y |   |Z| |Z|    
              .'  _\  '-' '-'    
            .'--.(A     ,__, )      
                  '-.     _.'        \033[91m
                    '----
                                                                                                            
..{}:: Name : port-scanner ::{}..\033[93m
..{}:: Version: 1.6 ::{}..\033[95m
..{}:: scripter: yazdan321 ::{}..\033[97m
..{}:: Tozihat: script bedone hich gone bug va kamelan farsi ast::{}..\033[94m
..{}:: Baraye Khoroj,Az Enter Estefade Konid::{}..\033[92m
 '''
print (banner)

remoteserver = input("lotfan ip or address ra bedahid ta scan ra shoro konam.address : \033[99m")
remoteserverip = socket.gethostbyname(remoteserver)

if remoteserver == "":
        sys.exit()

print ("lotfan montazer bemanid...ip sit shoma : ", remoteserverip)

t1 = datetime.now()

try:
    for port in range (1,200):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        natije = sock.connect_ex((remoteserverip,port))
        if natije == 0:
            print("*-*"*27)
            print("port {} :         open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("shoma kelidi az roye keyboard zadid ke marbot be barname nabod :/")
    sys.exit()

except socket.gaierror:
    print("nemitavanam be sit'i ke dadi motasel shod")
    sys.exit()

except socket.error:
    print("server eshtebah ast!!")
    sys.exit()

t2 = datetime.now()

t3 = t2 - t1

print ("scan tamam shod dar : ", t3)

banner = '''

      bbbbbbbbbbbb                               
      bbb     bbbb     bbbbb      bbbbb     bbbbbbbbb 
      bbbbbbbbbbbb       bbbb    bbbbb      bbb   bbb
      bbb     bbbb          bbbb            bbbbbbbbb    
      bbb     bbbb         bbbb             bbb        
      bbbbbbbbbbbb        bbbb              bbbbbbbbb 
     ''' 
print (banner)

input("Thank you for using the app")


