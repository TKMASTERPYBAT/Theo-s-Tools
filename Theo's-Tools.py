import os
from colorama import Fore, init
import time

def banner():
    print(Fore.RED + '''


.___..  ..___.__. * __.  .___..__..__..    __.  
  |  |__|[__ |  | '(__     |  |  ||  ||   (__   
  |  |  |[___|__|  .__)    |  |__||__||___.__)  
                                              


''')
    print(Fore.RED + "[+] MAKE SURE YOUR RUNNING THIS TOOL AS ROOT!")
    print("")
    print("")
    print(Fore.CYAN + "1) WireShark")
    print(Fore.BLUE + "2) Nmap")
    print(Fore.GREEN + "3) Hydra")
    print(Fore.YELLOW + "4) John The Ripper")
    print(Fore.RED + "5) Social-Engineer-Tool-Kit")
    print(Fore.BLUE + "6) aircrack-ng")
    print(Fore.RED + "00) Exit")
    print("")

def ws():
  os.system('clear')
  print(Fore.BLUE + "1) Install")
  print(Fore.BLUE + "2) Run")
  print(Fore.BLUE + "99) Go Back")

  ws = input("Enter Option => ")

  if ws == "1":
     os.system('sudo apt install wireshark')
     input("Press Enter To Continue...")
  elif ws == "2":
     os.system('sudo wireshark')
     input("Press Enter To Continue...")
  elif ws == "99":
     main()
  else:
     print(Fore.RED + "[-] Invalid Option!")
     time.sleep(2)

def nm():
  os.system('clear')
  print(Fore.BLUE + "1) Install")
  print(Fore.BLUE + "2) Run")
  print(Fore.BLUE + "99) Go Back")

  nm = input("Enter Option => ")

  if nm == "1":
     os.system('sudo apt install nmap')
     input("Press Enter To Continue...")
  elif nm == "2":
     os.system('sudo nmap')
     input("Press Enter To Continue...")
  elif nm == "99":
     main()
  else:
     print(Fore.RED + "[-] Invalid Option!")
     time.sleep(2)

def hy():
  os.system('clear')
  print(Fore.BLUE + "1) Install")
  print(Fore.BLUE + "2) Run")
  print(Fore.BLUE + "99) Go Back")

  hy = input("Enter Option => ")

  if hy == "1":
     os.system('sudo apt install hydra')
     input("Press Enter To Continue...")
  elif hy == "2":
     os.system('sudo hydra')
     input("Press Enter To Continue...")
  elif hy == "99":
     main()
  else:
     print(Fore.RED + "[-] Invalid Option!")
     time.sleep(2)

def jn():
  os.system('clear')
  print(Fore.BLUE + "1) Install")
  print(Fore.BLUE + "2) Run")
  print(Fore.BLUE + "99) Go Back")

  jn = input("Enter Option => ")

  if jn == "1":
     os.system('sudo apt install john')
     input("Press Enter To Continue...")
  elif jn == "2":
     os.system('sudo john')
     input("Press Enter To Continue...")
  elif jn == "99":
     main()
  else:
     print(Fore.RED + "[-] Invalid Option!")
     time.sleep(2)

def set():
  os.system('clear')
  print(Fore.BLUE + "1) Install")
  print(Fore.BLUE + "2) Run")
  print(Fore.BLUE + "99) Go Back")

  set = input("Enter Option => ")

  if set == "1":
     os.system('sudo apt install set')
     input("Press Enter To Continue...")
  elif set == "2":
     os.system('sudo setoolkit')
     input("Press Enter To Continue...")
  elif set == "99":
     main()
  else:
     print(Fore.RED + "[-] Invalid Option!")
     time.sleep(2)

def ac():
  os.system('clear')
  print(Fore.BLUE + "1) Install")
  print(Fore.BLUE + "2) Run")
  print(Fore.BLUE + "99) Go Back")

  ac = input("Enter Option => ")

  if ac == "1":
     os.system('sudo apt install aircrack-ng')
     input("Press Enter To Continue...")
  elif ac == "2":
     os.system('sudo aircrack-ng')
     input("Press Enter To Continue...")
  elif ac == "99":
     main()
  else:
     print(Fore.RED + "[-] Invalid Option!")
     time.sleep(2)

def main():
   while True:
      os.system('clear')
      banner()
      choice = input(Fore.CYAN + "Enter Choice => ")

      if choice == "1":
         ws()
      elif choice == "2":
         nm()
      elif choice == "3":
         hy()
      elif choice == "4":
         jn()
      elif choice == "5":
         set()
      elif choice == "6":
         ac()
      elif choice == "00":
         break
      
if __name__ == "__main__":
   main()