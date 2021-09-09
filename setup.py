import os

file = open("packages.txt", "r")

for line in file:
    print('[*] Collecting Packages!')
    os.system('pip install ' + line)
    print('\n[!] You should now be able to use the phoneinfo.py script')
    
file.close()
