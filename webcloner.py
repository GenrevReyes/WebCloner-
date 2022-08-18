import urllib.request
from time import sleep
from termcolor import colored
from pyfiglet import figlet_format as logo
import os
import time
import sys
#Class Colors

red='\033[1;31m' #
green='\033[1;32m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'
sky='\033[1;36m'



def chmod():
    Termux_data = True
    os.system('chmod +x webcloner.py') #Chmod setup

def netcheck(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #request open
        return True
    except:
        return False


chmod() #chmod here
def Slow(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.2/30)



def slow(f):
    for d in f + '\n':
        sys.stdout.write(d)
        sys.stdout.flush()
        time.sleep(0.8/15)


def Display():
    text = logo('WebCloner')
    res = colored(text, 'yellow')
    Slow(f'{res}{yellow}Author:{sky}Genrev-reyes13{red}              version1.9')


def about():
    print(f'{sky}Author:{red} Genrev-reyes13')
    print(f'{sky}Facebook:{red} https://www.facebook.com/genrev.reyes.16')
    print(f'{sky}Facebook Group:{red} TermuxPhilippines')
    print(f'{sky}Github: {red}GenrevReyes')
    print(f'{sky}Tool_name:{red} WebCloner')
    loop = input(" ")
    os.system('python webcloner.py')
sleep(0.5)
os.system('clear')
sleep(1)
Display()
print(' ')
print(f'{yellow}[*]1.WebCloner')
print(' ')
print(f'{yellow}[*]2.About')
print(' ')
print(f'{yellow}[*]3.Join on group')
print(' ')
print(f'{yellow}[*]4.Exit')
print(' ')
choice = input("Enter: ")

if not choice in ('1', '2', '3', '4'):
    os.system('termux-vibrate -d 100')
    slow(f'{red}[!]Invalid Input! ')
    os.system('python webcloner.py')
if choice == '1':

    slow(f'{purple}Please Wait')
    sleep(2)
    print(' ')
    Termux = True
    if Termux == False:
        sys.exit('Thanks For using')
    if Termux == True:
        url = input(f"{green}Website url: ")                                                                                                         sleep(3)
        print(' ')
        path = input(f'{green}Enter any name to create file: ')
        print(' ')
        sleep(2)
        slow(f'{yellow}[*]Creating File Please Wait')
        print(' ')
        sleep(5)
        slow(f'{blue}[✓]Succesfully Created ')
        sleep(2)
        print(' ')
        slow(f'{purple}[*]Founding url')
        sleep(4)
        netcheck()
        print(' ')
        slow(f'{yellow}[✓]Founding Succes')

        if not netcheck():
            os.system('termux-vibrate -d 100')
            slow(f'{red}[!]Founding error No Internet')
        else:
            slow(f'{sky}[*]Decoding {blue}{url}')
            sleep(5)
            netcheck()
            if netcheck():
                print(' ')
                website_data = urllib.request.urlopen(url)
                html = website_data.read()
                html = html.decode()
                slow(f'{yellow}[✓]Decoding succes')
                sleep(1)

                with open(path, 'w') as c:
                    c.write(html)
                print(' ')

                slow(f'{sky}[*]Succesfully save in {path}')
                print(' ')
                slow(f'{green}[*]Check your {path}')
            else:
                os.system('termux-vibrate -d 100')
                slow(f'{red}[!]Decoding error No Internet')
                os.system('exit')
if choice == '2':
    about()

if choice == '3':

    os.system('termux-open-url https://www.facebook.com/groups/427631411331889/?ref=share')
    sleep(1)
    os.system('python webcloner.py')


if choice == '4':
    slow(f'{yellow}Thanks for using')
    sys.exit()
