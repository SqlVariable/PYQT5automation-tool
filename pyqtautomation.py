import os
from colorama import *

print("WELCOME TO PYQT5automation-tool v0.0.1")

class pyqt5cli:
    def __init__(self):
        self.virtualenvironment_name = ''
#$ cd <envname>
#$ Scripts\activate 
    def virtual_environment(self):
        try:
            self.virtualenvironment_name = input('virtual-enviroment-name::')
            os.system('virtualenv '+self.virtualenvironment_name)
        except:
            print(Fore.RED+"<!-ERROR-!>")

    def activate_virtualenvironment(self):
        if virtualenvironment_name == '':
            return None
        try:
            os.system('cd '+self.virtualenvironment_name)
            os.system('cd Scripts')
            os.system('activate')
            os.system('cd ..')
            os.system('cd ..')
        except:
            print(Fore.RED+"<!-ERROR-!>")
    def deactivate_virtualenvironment(self):
        try:
            os.system('cd '+self.virtualenvironment_name)
            os.system('cd Scripts')
            os.system('deactivate')
            os.system('cd ..')
            os.system('cd ..')
        except:
            print(Fore.RED+"<!-ERROR-!>")

    def get_uiTextToPyFile(self):
        try:
            ui_filename = input("filename::")
            output_filename = input("output-file-name::")
            os.system('pyuic5 -x '+ui_filename+' -o '+output_filename)
        except:
            print(Fore.RED+"<!-ERROR-!>")

    def get_help(self):
        print(Fore.BLUE+"uipy : getting ui files and add to current directory a python file that taken designer information in file with .ui extension")
        print(Fore.BLUE+"v : occuring a virtual enviroment to current directory")
        print(Fore.BLUE+"a : activating virtual environment")
        print(Fore.BLUE+"d : deactivating virtual environment")
        print(Fore.BLUE+"ls : list the all files in current directory")
        print(Fore.BLUE+"cat : read all lines in a file")
        print(Fore.BLUE+"msg : that write to a comment to console")
        print(Fore.BLUE+"quit : quitting the program")

    def list(self):
        os.system('dir')

    def read_file(self):
        filename = input('filename-to-read::')
        os.system('more '+filename)

    def message(self,message):
        print(Fore.BLUE+message)



CLI = pyqt5cli()


while True:
    inp = input(Fore.RED+'pyqt5>>>')
    if inp != "":
        print(Fore.GREEN+inp)
    if inp == "uipy":
        CLI.get_uiTextToPyFile()
    elif inp == "version":
        print(Fore.GREEN+"pyqt5automation-tool v0.0.1")
    elif inp == "help":
        CLI.get_help()
    elif inp == "v":
        CLI.virtual_environment()
    elif inp == "a":
        CLI.activate_virtualenvironment()
    elif inp == "d":
        CLI.deactivate_virtualenvironment()
    elif inp == "cat":
        CLI.read_file()
    elif inp == "msg":
        message = input('write-a-message::')
        CLI.message(message)
    elif inp == "clear":
        os.system('cls')
    elif inp == "ls":
        CLI.list()
    elif inp == "quit":
        break



print('good_bye :)')
stop = input('')
    
    


