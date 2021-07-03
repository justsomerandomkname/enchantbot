
import os
import time


filedirectory = input('What is the directory where your python project is in: ')
os.system('cd '+(filedirectory))
nameofexe = input('what do you wanna name your windows application: ')
os.rename('maker.py', nameofexe+'.py')
os.system('pyinstaller '+nameofexe+'.py')
time.sleep(1)
print(nameofexe+'.exe', 'made')

