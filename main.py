import os
import subprocess
from colorama import Fore, Style
from pyfiglet import Figlet

custom_fig = Figlet(font='graffiti')


winrar_path = "C:/Program Files/WinRAR/RAR.exe"
wordlist_path = "./wordlist/wordlist.txt"
files_directory = "./files"

print(custom_fig.renderText('AKASHY'))



rar_files = [file for file in os.listdir(files_directory) if file.endswith(".rar")]


for rar_file in rar_files:
    file_path = os.path.join(files_directory, rar_file)
    print(Fore.YELLOW + "Cracking file:", file_path, Style.RESET_ALL)
    with open(wordlist_path, "r") as wordlist_file:
        for password in wordlist_file:
            password = password.strip()
            print("Trying password:", password)
            result = subprocess.run([winrar_path, "x", "-p" + password, file_path], capture_output=True, text=True)
            if result.returncode == 0:
                print("Password found:", password)
                input("Press Enter to continue...")
                break
            else:
                print("Password failed:", password)