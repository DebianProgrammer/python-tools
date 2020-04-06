import sys
import colorama
import base64
import json
import requests
import random
import pyfiglet
from colorama import Fore, Back, Style
colorama.init()
args = sys.argv[1:]
possible = ["someone needs to use some tools", "green looks cool", "ascii art is cool", "im tired", "i need to chill", "ugh", "im bored"]
# print(Fore.GREEN)
ascii_banner = pyfiglet.figlet_format(random.choice(possible))
#class bcolors:
#    HEADER = '\033[95m'
#    OKBLUE = '\033[94m'
#    OKGREEN = '\033[92m'
#    WARNING = '\033[93m'
#    FAIL = '\033[91m'
#    ENDC = '\033[0m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'
helpmsg = "Commands:\n--help for this message\n--base64 <decode|encode> - encode or decode base64\n--dog - get random dog\n--gethttp - get data from a website\n--random <min> <max> - get random number between 2 numbers\n--asciiart - make ascii art out of text"
print(str(sys.argv))
def noargs():
    print(Fore.BLUE)
    print("--help for help")
    quit()

if args:
    if(sys.argv[1] == "--help"):
        print(Fore.GREEN)
        print(ascii_banner)
        print(Fore.CYAN)
        print(helpmsg)
        quit()
    if(sys.argv[1] == "--random"):
        if(len(sys.argv) == 2):
            print(Fore.RED)
            print("Invalid args! use --help for help, the syntax for this command is: --random <min> <max>")
            quit()
        if(len(sys.argv) == 3):
            print(Fore.RED)
            print("Invalid args! use --help for help, the syntax for this command is: --random <min> <max>")
            quit()
        mininum = int(sys.argv[2])
        maxnum = int(sys.argv[3])
        number = random.randrange(mininum, maxnum)
        print(Fore.GREEN)
        print("Got random number!")
        print(" ")
        print(number)
        quit()
    if(sys.argv[1] == "--gethttp"):
        print(Fore.GREEN)
        print("getting website data.. Please wait!")
        print(Style.RESET_ALL)
        if(len(sys.argv) == 2):
            print(Fore.RED)
            print("Invalid args! use --help for help, the syntax for this command is: --gethttp <link>")
            quit()
        r = requests.get(sys.argv[2])
        s = str(r.status_code)
        s2 = str(r.headers)
        s3 = str(r.encoding)
        if(r.status_code == 200):
            print(Fore.GREEN)
            print("Got response HTTP 200 OK")
            print("Requests data:")
            print(" ")
            print("Status code: " + s)
            print(" ")
            print("Headers: " + s2)
            print(" ")
            print("Encoding: " + s3)
            print(" ")
            seq = ["Status Code: " + s + "\n", "Headers: " + s2 + "\n", "Encoding: " + s3 + "\n", r.text + "\n"]
            filename = input("To see what the server returened please type a file name: ")
            obj = open(filename, "w")
            obj.writelines(seq)
            obj.close()
        quit()
    if(sys.argv[1] == "--base64"):
        if(len(sys.argv) == 2):
            print(Fore.RED)
            print("Invalid args! use --help for help, the syntax for this command is: --base64 <encode|decode> <string>")
            quit()
        if(sys.argv[2] == "encode"):
            #print("you want to encode")
            argbytes = sys.argv[3].encode('ascii')
            basebytes = base64.b64encode(argbytes)
            basestr = basebytes.decode('ascii')
            obj = open("encoded.txt", "w")
            obj.write(basestr)      
            obj.close()
            print(Fore.GREEN)
            print("Success! Wrote encoded data to encoded.txt.")
            quit()
        if(sys.argv[2] == "decode"):
            #print("You want to decode")
            argbasebytes = sys.argv[3].encode('ascii')
            decodedbasebytes = base64.b64decode(argbasebytes)
            decodedstr = decodedbasebytes.decode('ascii')
            deobj = open("decoded.txt", "w")
            deobj.write(decodedstr)
            deobj.close()
            print(Fore.GREEN)
            print("Success! Wrote decoded data to decoded.txt")
            quit()
        else:
            print(Fore.RED)
            print("Invalid args! use --help for help, the syntax for this command is: --base64 <encode|decode> <string>")
        # print("Invalid args! use --help for help, the syntax for this command is: --base64 <encode|decode> <string>")
    if(sys.argv[1] == "--asciiart"):
        if(len(sys.argv) == 2):
            print(Fore.RED)
            print("Invalid args! Do --help for help, the args for this command are: --asciiart <string>")
            quit()
        asciiart2 = pyfiglet.figlet_format(sys.argv[2])
        print(asciiart2)
        print("What color do u want it in?")
        print("1. Default")
        print("2. Red")
        print("3. Green")
        print("4. Yellow")
        print("5. Cyan")
        print("6. Blue")
        print("7. Magenta")
        color = input("Choose: ")
        if(color == "1"):
            print(Fore.RESET)
            print(asciiart2)
            quit()
        if(color == "2"):
            print(Fore.RED)
            print(asciiart2)
            quit()
        if(color == "3"):
            print(Fore.GREEN)
            print(asciiart2)
            quit()
        if(color == "4"):
            print(Fore.YELLOW)
            print(asciiart2)
            quit()
        if(color == "5"):
            print(Fore.CYAN)
            print(asciiart2)
            quit()
        if(color == "6"):
            print(Fore.BLUE)
            print(asciiart2)
            quit()
        if(color == "7"):
            print(Fore.MAGENTA)
            print(asciiart2)
            quit()
        else:
            print("well u did not choose so i chose for you")
            print(Fore.RESET)
            print(asciiart2)
            quit()
        # asciiart2 = pyfiglet.figlet_format(sys.argv[2])
        # print(asciiart2)
        quit()
else:
    noargs()